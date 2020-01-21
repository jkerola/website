from flask import Blueprint, render_template, redirect, flash, url_for
from flaskblog.forms import LoginForm, ReportForm

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    report_form = ReportForm()
    if login_form.validate_on_submit():
        flash('Welcome back.', 'success')
        return redirect(url_for('main.home'))
    elif login_form.errors:
        flash('Please check your credentials.', 'warning')
    return render_template('login.html', title='Login', login_form=login_form, report_form=report_form)