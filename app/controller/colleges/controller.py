from os import name
from flask.helpers import url_for
from app.controller.colleges.forms import CollegeForm 
from flask import render_template, redirect, request, jsonify, flash
from . import college
import app.models.college as CollegeModel



@college.route("/college")
def index():
    colleges = CollegeModel.Colleges.all()
    print(colleges)
    return render_template("college/index.html", colleges=colleges)


@college.route("/college/create", methods=['POST', 'GET'])
def create():
    form = CollegeForm(request.form)
    if request.method == 'POST' and form.validate():
        college = CollegeModel.Colleges(code=form.code.data, name=form.name.data)
        college.add()
        return redirect('/college')
    else:
        return render_template('college/create.html', form=form)


@college.route('/college/edit/<id>', methods=['POST', 'GET'])
def edit_college(id):
    college = CollegeModel.Colleges.edit(id)
    return render_template('college/edit.html', data=college[0])

@college.route('/college/update/<id>', methods=['POST'])
def update_college(id):
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        course = CollegeModel.Colleges.update(id, code, name)
        return redirect(url_for('.index'))