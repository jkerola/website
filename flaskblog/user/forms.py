'''User forms module'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    '''Login form for the login page'''
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

class UpdateInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=32)])
    real_name = StringField('Real name', validators=[DataRequired(), Length(min=1, max=128)])
    email_personal = StringField('Personal Email', validators=[DataRequired(), Email(), Length(min=1, max=128)])
    email_company = StringField('Company Email', validators=[DataRequired(), Email(), Length(min=1, max=128)])
    current_pass = PasswordField('Current Password', validators=[DataRequired()])

    submit = SubmitField('Update')

