'''User specific forms module.'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    '''Login form for the login page. [username, password, submit]'''
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

class UpdateInfoForm(FlaskForm):
    '''Change user account details on the acount page.
    [username, real_name, email_company, email_personal, current_pass, submit]'''
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=32)])
    real_name = StringField('Real name', validators=[DataRequired(), Length(min=1, max=128)])
    email_personal = StringField('Personal Email', validators=[DataRequired(), Email(), Length(min=1, max=128)])
    email_company = StringField('Company Email', validators=[DataRequired(), Email(), Length(min=1, max=128)])
    current_pass = PasswordField('Current Password', validators=[DataRequired()])

    submit = SubmitField('Update')

