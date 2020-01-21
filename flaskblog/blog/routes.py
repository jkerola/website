'''routes for the main package'''
from flask import Blueprint, render_template, url_for, redirect, flash, request
from flaskblog.main.forms import ReportForm

blog = Blueprint('blog', __name__)

@blog.route('/blog', methods=['GET'])
def main():
    '''render the blog page'''
    report_form = ReportForm()
    return render_template('blog.html', title='Blog', report_form=report_form)