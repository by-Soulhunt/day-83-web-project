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


def group_data_for_template(object_list):
    """
    Group skills by 3 elements into nested list
    :param object_list:
    :return:  grouped_list, nested list with grouped objects by 3 elements
    """
    grouped_list = []
    for i in range(0, len(object_list), 3):
        # Create a group of 3 elements (or less if there is a remainder)
        grouped_list.append(object_list[i:i + 3])

    return grouped_list


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
    # Experience data
    experience = db.session.execute(db.Select(Experience))
    all_experience = experience.scalars().all()

    # Education data
    education = db.session.execute(db.Select(Education))
    all_education = education.scalars().all()

    # Skills data
    skills = db.session.execute(db.Select(Skills))
    all_skills = skills.scalars().all()
    grouped_list = group_data_for_template(all_skills)

    # Languages data
    languages = db.session.execute(db.Select(Language))
    languages = languages.scalars().all()
    all_languages = group_data_for_template(languages)

    return render_template("resume.html",
                           all_experience=all_experience,
                           all_education=all_education,
                           all_skills=all_skills,
                           all_languages=all_languages,
                           grouped_list=grouped_list
                           )


@app.route("/projects")
def projects():
    """
    Takes projects data from DataBase and show in template
    :return: projects.html
    """
    result = db.session.execute(db.Select(Projects))
    all_projects = result.scalars().all()
    return render_template("projects.html", all_projects=all_projects)


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