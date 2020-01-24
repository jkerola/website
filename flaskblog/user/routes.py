from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.main.forms import ReportForm
from flaskblog.user.forms import LoginForm
from flaskblog.models import User

user = Blueprint('user', __name__)

#Adapted from Corey Schafers (coreyMS.com) excellent Flask tutorials 
@user.route('/login', methods=['GET', 'POST'])
def login():
    '''Checks given credentials against database, logs user in if correct.'''
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    login_form = LoginForm()
    report_form = ReportForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Welcome back.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Please check your credentials.', 'warning')
    return render_template('login.html', title='Login', login_form=login_form, report_form=report_form)

@user.route('/logout', methods=['GET'])
def logout():
    '''log the current user out'''
    logout_user()
    return redirect(url_for('main.home'))

@user.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    '''account details page for updating info'''
    report_form = ReportForm()
    return render_template('account.html', title='Account Settings', report_form=report_form)