from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class ReportForm(FlaskForm):
    '''report form for footer report button, website issues'''
    title = StringField('Issue', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    content = TextAreaField('Description', validators=[DataRequired()])

    submit = SubmitField('Send Report')

class LoginForm(FlaskForm):
    '''Login form for the login page'''
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')