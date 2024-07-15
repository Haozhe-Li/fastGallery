from flask import Flask, render_template, request, redirect, url_for
from core.rander import rander

app = Flask(__name__)


@app.route("/")
def home():
    content, enable_search_bar = rander()
    no_result = (content["pic"] == "")
    return render_template("index.html", **content, search_bar=enable_search_bar, no_result=no_result)


@app.route("/filter/<keyword>")
def filter(keyword):
    keyword = keyword.lower()
    content, enable_search_bar = rander(keyword=keyword)
    no_result = (content["pic"] == "")
    return render_template("index.html", **content, search_bar=enable_search_bar, no_result=no_result)


@app.route("/search")
def search():
    query = request.args.get("query", "")
    if query == "":
        return redirect("/")
    return redirect(url_for("filter", keyword=query))


if __name__ == "__main__":
    app.run(debug=True)
