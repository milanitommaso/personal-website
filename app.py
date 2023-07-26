# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, g
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import json
from visit_tracker import track_visit

DEPLOY = True
app = Flask(__name__)
app.config["DEBUG"] = True

# connect to the database
with open('mysql_settings.json') as settings:
    mysql_settings = json.load(settings)

#database
app.config['MYSQL_DATABASE_HOST'] = mysql_settings["host"]
app.config['MYSQL_DATABASE_PORT'] = mysql_settings["port"]
app.config['MYSQL_DATABASE_USER'] = mysql_settings["user"]
app.config['MYSQL_DATABASE_PASSWORD'] = mysql_settings["password"]
app.config['MYSQL_DATABASE_DB'] = mysql_settings["database"]

mysql = MySQL(cursorclass = DictCursor)
mysql.init_app(app)

@app.before_request
def before_request():
    g.db_conn = mysql.connect()

@app.after_request
def after_request(response):
    if hasattr(g, "db_conn"):
        g.db_conn.close()

    return response

@app.route("/github")
def github():
    # track the visit
    if DEPLOY: 
        track_visit(g.db_conn, request, page="github")

    return redirect("https://github.com/milanitommaso")

@app.route("/github/<repository>")
def github_repository(repository):
    # track the visit
    if DEPLOY:
        track_visit(g.db_conn, request, page="github")

    return redirect("https://github.com/milanitommaso/{}".format(repository))

@app.route("/linkedin")
def linkedin():
    # track the visit
    if DEPLOY:
        track_visit(g.db_conn, request, page="linkedin")

    return redirect("https://www.linkedin.com/in/milani-tommaso/")

@app.route("/")
def index():
    # track the visit
    if DEPLOY:
        track_visit(g.db_conn, request, page="index")

    return render_template("index.html")

@app.route("/resume")
def resume():
    # track the visit
    if DEPLOY:
        track_visit(g.db_conn, request, page="resume")

    return render_template("resume.html")

@app.route("/projects")
def projects():
    # track the visit
    if DEPLOY:
        track_visit(g.db_conn, request, page="projects")

    return render_template("projects.html")

@app.route("/contact")
def contact():
    # track the visit
    if DEPLOY:
        track_visit(g.db_conn, request, page="contact")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
