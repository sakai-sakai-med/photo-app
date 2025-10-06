from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/upload', methods=['POST'])
def upload():
    name = request.form['name']
    photo = request.files['photo']
    if photo:
        filename = f"{name}_{photo.filename}"
        photo.save(os.path.join(UPLOAD_FOLDER, filename))
        return render_template('success.html', name=name, filename=filename)
    return 'アップロード失敗'

if __name__ == '__main__':
    app.run(debug=True)