from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import college
import app.models as models


@college.route("/college")
def index():
    # students = models.Students.all()
    return render_template("college/index.html")

@college.route("/create")
def create():
    return render_template("college/create.html")