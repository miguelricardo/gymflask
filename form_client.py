from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,HiddenField,PasswordField
from wtforms.validators import DataRequired

class FormClient(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    save = SubmitField('Save')