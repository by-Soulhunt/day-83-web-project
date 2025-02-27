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
    """Main page"""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5003)