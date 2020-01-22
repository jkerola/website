'''routes for the main package'''
from flask import Blueprint, render_template, url_for, redirect, flash, request
from flaskblog import storage
from flaskblog.main.forms import ReportForm

blogging = Blueprint('blog', __name__)

@blogging.route('/blog', methods=['GET'])
def blog():
    report_form = ReportForm()
    posts = storage.get_posts()
    return render_template('blog.html', title='Blog', posts=posts, report_form=report_form)