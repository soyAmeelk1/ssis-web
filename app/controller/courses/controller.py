from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import course
import app.models.course as CourseModel
import app.models.college as CollegeModel

from app.controller.courses.forms import CourseForm 

@course.route("/course")
def index():
    courses = CourseModel.Courses.all()
    print(courses)
    return render_template("course/index.html", courses=courses)



@course.route('/course/create', methods=['POST', 'GET'])
def create():
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        course = CourseModel.Courses(code=form.name.data, name=form.code.data, college=form.college_id.data)
        print(course)
        course.add()
        return redirect('.index')
    else:
        colleges = CollegeModel.Colleges.refer()
        return render_template("course/create.html", form=form, data=colleges)