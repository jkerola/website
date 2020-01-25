'''routes for the main package'''
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect, flash, request
from flaskblog import db
from flaskblog.main.forms import ReportForm, ContactForm
from flaskblog.main.utils import send_report_notification, send_contact_notification
from flaskblog.models import Post, Report
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

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    '''render the contact report_form page'''
    report_form = ReportForm()
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        title = contact_form.title.data
        content = contact_form.content.data
        send_contact_notification(name, title, email, content)
        flash('Message sent!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', contact_form=contact_form, report_form=report_form)

@main.route('/report', methods=['GET', 'POST'])
def report():
    '''report contact form for website issues'''
    report_form = ReportForm(request.form)
    if report_form.validate_on_submit():
        title = report_form.title.data
        email = report_form.email.data
        content = report_form.content.data
        date = datetime.utcnow()
        report = Report(
            title = title,
            email = email,
            content = content,
            date_posted = date
        )
        send_report_notification(title, content, email, date)
        db.session.add(report)
        db.session.commit()

        flash('Report submitted succesfully. Thank you!', 'success')
    else:
        flash(f'Report submission failed. Please check your email address.', 'warning')
    return redirect(request.referrer)
