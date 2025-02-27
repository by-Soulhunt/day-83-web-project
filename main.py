from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
import os


# Flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap(app)


# Routs
@app.route("/")
def index():
    """
    Main page
    :return: template index.html
    """
    return render_template("index.html")


@app.route("/resume")
def resume():
    """
    Resume page
    :return: template resume.html
    """
    return render_template("resume.html")


@app.route("/projects")
def projects():
    """
    Projects page
    :return: template projects.html
    """
    return render_template("projects.html")


@app.route("/contact")
def contact():
    """
    Contact page
    :return: template contact.html
    """
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True, port=5003)