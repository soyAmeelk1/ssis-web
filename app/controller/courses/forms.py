from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import app.models.course as models

class CourseForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    code = StringField('Code', [validators.DataRequired()])
    college_id = StringField('College_id', [validators.DataRequired()])
    submit = SubmitField("Submit")