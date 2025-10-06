from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    main_csv_path = r"\\126.0.3.173\ms-sv\三好製造課（管理者：井戸課長）\DXでじとら\冷間転造IOT\main.csv"
    df = pd.read_csv(main_csv_path)

    df_sorted = df.sort_values("時間")
    df_latest = df_sorted.groupby("設備").tail(1)
    data = df_latest.to_dict(orient="records")

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
