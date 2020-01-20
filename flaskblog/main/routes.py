'''routes for the main package'''
from flask import Blueprint, render_template, url_for

#blueprint for all general routes
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    '''render home page'''
    return render_template('home.html')

@main.route("/profile")
def profile():
    '''render the porfolio page'''
    return render_template('profile.html', title='Profile')