from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homapage():
    return "<h1>Welcome to shop</h1>"

@app.route("/types")
def types():
    return render_template("types.html")

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html")

@app.route("/sale/<name>")
def sale(name):
    name = name.capitalize()
    return render_template("sale.html", name=name)