# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import datetime
import hashlib

app = Flask(__name__)
app.config["DEBUG"] = True


@app.before_request
def before_request():
    # log the request
    timestamp = datetime.datetime.now()
    hashed_ip = hashlib.md5(request.remote_addr.encode()).hexdigest()

    with open("logs.txt", "a") as f:
        f.write(f"{timestamp} - {hashed_ip} - {request.method} - {request.url}\n")


@app.route("/github")
def github():
    return redirect("https://github.com/milanitommaso")

@app.route("/github/<repository>")
def github_repository(repository):
    return redirect("https://github.com/milanitommaso/{}".format(repository))

@app.route("/linkedin")
def linkedin():
    return redirect("https://www.linkedin.com/in/milani-tommaso/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
