#!/usr/bin/env python

from flask import Flask
from flask import render_template
from menu import generatemenu

app = Flask(__name__)

@app.route("/")
def fruit():
    """Return random fruit"""

    menu = generatemenu()
    return render_template("menu_format.html", title="Dinner Recommendation at Young Joni", meal=menu)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
