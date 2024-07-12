from flask import Flask, render_template
from core.rander import rander

app = Flask(__name__)


@app.route("/")
def home():
    content = rander()
    return render_template("index.html", **content)


@app.route("/filter/<keyword>")
def filter(keyword):
    keyword = keyword.lower()
    content = rander(keyword=keyword)
    return render_template("index.html", **content)


if __name__ == "__main__":
    app.run(debug=True)
