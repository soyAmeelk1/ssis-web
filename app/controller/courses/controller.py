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
        course = CourseModel.Courses(code=form.name.data, name=form.code.data, college_id=form.college_id.data)
        course.add()
        return redirect('/course')
    else:
        colleges = CollegeModel.Colleges.refer()
        return render_template("course/create.html", form=form, data=colleges)
    
@course.route('/course/edit/<id>', methods=['POST', 'GET'])
def edit_course(id):
    course = CourseModel.Courses.edit(id)
    colleges = CollegeModel.Colleges.refer()
    return render_template('course/edit.html', data=course[0], datas=colleges)

@course.route('/course/update/<id>', methods=['POST'])
def update_course(id):
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        college = request.form['college']

        course = CourseModel.Courses.update(id, code, name, college)
        return redirect(url_for('.index'))