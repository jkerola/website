'''routes for the main package'''
from flask import Blueprint, render_template

#blueprint for all general routes
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    '''render home page'''
    return render_template('home.html')
