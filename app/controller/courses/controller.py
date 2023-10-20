from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import course
import app.models as models


@course.route("/course")
def index():
    # students = models.Students.all()
    return render_template("course/index.html")

@course.route("/create")
def create():
    return render_template("course/create.html")