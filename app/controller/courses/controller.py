from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import course
import app.models.course as CourseModel


@course.route("/course")
def index():
    courses = CourseModel.Courses.all()
    print(courses)
    return render_template("course/index.html", courses=courses)

@course.route("/create")
def create():
    return render_template("course/create.html")