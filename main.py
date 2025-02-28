from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
import datetime
import os


# Flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap(app)


# Create DataBase
class Base(DeclarativeBase):
    """Declarative class"""
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main_db.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure tables
class Projects(db.Model):
    """
    Projects DB table
    """
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class Experience(db.Model):
    """
    Experience DB table
    """
    __tablename__ = "experience"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    position: Mapped[str] = mapped_column(String(100), nullable=False)
    organization: Mapped[str] = mapped_column(String(250), nullable=False)
    org_address: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)


class Education(db.Model):
    """
    Education DB table
    """
    __tablename__ = "education"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    education_institution: Mapped[str] = mapped_column(String(100), nullable=False)
    institution_address: Mapped[str] = mapped_column(String(250), nullable=False)
    major: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)


class Skills(db.Model):
    """
    Skills DB table
    """
    __tablename__ = "skills"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    skills: Mapped[str] = mapped_column(String(250), nullable=False)


class Language(db.Model):
    """
    Language DB table
    """
    __tablename__ = "language"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    language: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


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


@app.context_processor
def inject_date():
    """
    :return: Add date variable into all templates
    """
    return {"date":datetime.datetime.now().year}


if __name__ == '__main__':
    app.run(debug=True, port=5003)