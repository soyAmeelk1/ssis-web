from os import name
from flask.helpers import url_for
# from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import student
import app.models.student as StudentModel
import app.models.course as CourseModel
from app.controller.students.forms import StudentForm 


@student.route("/")
@student.route("/student")
def index():
    students = StudentModel.Students.all()
    return render_template("student/index.html", students=students)

@student.route("/student/create", methods=['POST', 'GET'])
def create_student():
    form = StudentForm(request.form)
    if request.method == 'POST' and form.validate():
        student = StudentModel.Students(id_number=form.id_number.data, first_name=form.first_name.data, last_name=form.last_name.data, course_id=form.course_id.data, year=form.year.data, gender=form.gender.data)
        student.add()
        return redirect('/')
    return render_template("student/create.html", form=form)
    
@student.route("/student/edit/<id>", methods=['POST', 'GET'])
def edit_student(id):
    student = StudentModel.Students.edit(id)
    course = CourseModel.Courses.refer()
    return render_template("student/edit.html", data=student[0], datas=course)

@student.route('/student/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        id_number = request.form['id_number']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']

        student = StudentModel.Students.update(id, id_number, first_name, last_name, course, year, gender)
        return redirect(url_for('.index'))