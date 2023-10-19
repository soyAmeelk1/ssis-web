from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import student
import app.models as models


@student.route("/")
@student.route("/student")
def index():
    # students = models.Students.all()
    return render_template("student/index.html")

@student.route("/create")
def create():
    return render_template("student/create.html")