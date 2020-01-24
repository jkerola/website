'''routes for the main package'''
from flask import Blueprint, render_template, url_for, redirect, flash, request
from flaskblog.main.forms import ReportForm
from flaskblog.models import Post
#blueprint for all general routes
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home', methods=['GET'])
def home():
    '''render home page'''
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2, page=page)
    report_form = ReportForm()
    return render_template('home.html', posts=posts, report_form=report_form), 200

@main.route('/profile', methods=['GET'])
def profile():
    '''render the porfolio page'''
    report_form = ReportForm()
    return render_template('profile.html', title='Profile', report_form=report_form)

@main.route('/contact', methods=['GET'])
def contact():
    '''render the contact report_form page'''
    report_form = ReportForm()
    return render_template('contact.html', title='Contact', report_form=report_form)

@main.route('/report', methods=['GET', 'POST'])
def report():
    '''report contact form for website issues'''
    report_form = ReportForm(request.form)
    if report_form.validate_on_submit():
        flash('Report submitted succesfully. Thank you!', 'success')
    else:
        flash(f'Report submission failed. Please check your email address.', 'warning')
    return redirect(request.referrer)