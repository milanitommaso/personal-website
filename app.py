# app.py

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/github")
def github():
    return redirect("https://github.com/milanitommaso")

@app.route("/linkedin")
def linkedin():
    return redirect("https://www.linkedin.com/in/milani-tommaso/")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
