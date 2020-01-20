'''routes for the main package'''
from flask import Blueprint, render_template, url_for

#blueprint for all general routes
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home', methods=['GET'])
def home():
    '''render home page'''
    return render_template('home.html')

@main.route('/profile', methods=['GET'])
def profile():
    '''render the porfolio page'''
    return render_template('profile.html', title='Profile')

@main.route('/blog', methods=['GET'])
def blog():
    '''render the blog page'''
    return render_template('blog.html', title='Blog')

@main.route('/contact', methods=['GET'])
def contact():
    '''render the contact form page'''
    return render_template('contact.html', title='Contact')