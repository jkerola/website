'''General use forms module'''
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class ReportForm(FlaskForm):
    '''report form for footer report button, website issues'''
    title = StringField('Issue', validators=[DataRequired(), Length(min=1, max=128)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=1, max=128)])
    content = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=1024)])

    submit = SubmitField('Send Report')

class ContactForm(FlaskForm):
    '''Contact me form'''
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=128)])
    title = StringField('Subject', validators=[DataRequired(), Length(min=1, max=128)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=128), Email()])
    content = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=3000)])

    submit = SubmitField('Send Message')