from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import college
import app.models.college as CollegeModel


@college.route("/college")
def index():
    colleges = CollegeModel.Colleges.all()
    print(colleges)
    return render_template("college/index.html", colleges=colleges)

@college.route("/create")
def create():
    return render_template("college/create.html")