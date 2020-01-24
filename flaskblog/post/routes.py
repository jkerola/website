'''routes for the post package'''
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect, flash, request, flash
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.main.forms import ReportForm
from flaskblog.models import Post
from sqlalchemy import extract

post = Blueprint('post', __name__)

@post.route('/blog', methods=['GET'])
def blog():
    '''default blog view, shows all posts'''
    report_form = ReportForm()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3, page=page)
    return render_template('blog.html', title='Blog', posts=posts, page=page, report_form=report_form)

@post.route('/blog/editor', methods=['GET', 'POST'])
@login_required
def editor():
    '''create new posts, edit existing ones.'''
    form = 0
    report_form = ReportForm()
    if request.method == 'POST':
        form = request.form
        if form['title'] and form['content'] and form['tags']:
            post = Post(
                title = form['title'],
                content = form['content'],
                tags = form['tags'],
                author = current_user
            )
            db.session.add(post)
            db.session.commit()
            flash('New post posted!', 'success')
            return redirect(url_for('post.blog'))
        else:
            flash('Check your content fields!', 'warning')
            redirect(url_for('post.blog', form=form))
    return render_template('editor.html', form=form, report_form=report_form)

@post.route('/blog/filter', methods=['GET'])
def sort_by_tags():
    '''filter blog posts by given tag query parameters'''
    '''sort posts by given tag'''
    report_form = ReportForm()
    page = request.args.get('page', 1, type=int)
    month = request.args.get('month', 0, type=int)
    tags = request.args.get('tags', '', type=str)

    if month and tags:
        posts = Post.query.filter(extract('month', Post.date_posted)==month)\
            .filter(Post.tags.contains(tags))\
            .order_by(Post.date_posted.desc())\
            .paginate(per_page=3, page=page)
        return render_template('blog.html', report_form=report_form, page=page, posts=posts)

    elif tags and month == 0:
        posts = Post.query.filter(Post.tags.contains(tags))\
            .order_by(Post.date_posted.desc())\
            .paginate(per_page=3, page=page)
        return render_template('blog.html', report_form=report_form, posts=posts)
    
    elif month and tags == '':
        posts = Post.query.filter(extract('month', Post.date_posted)==month)\
            .order_by(Post.date_posted.desc())\
            .paginate(per_page=3, page=page)
        return render_template('blog.html', report_form=report_form, page=page, posts=posts)
    else:
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3, page=page)
        return render_template('blog.html', report_form=report_form, page=page, posts=posts)


@post.route('/blog/post/<int:post_id>', methods=['GET'])
def find_post(post_id):
    '''find a specific post for viewing'''
    report_form = ReportForm()
    post = Post.query.get(post_id)
    previous = request.referrer
    if previous == None:
        previous = url_for('main.home')
    return render_template('post.html', post=post, previous=previous, report_form=report_form)

@post.route('/blog/update/<int:post_id>', methods=['POST', 'GET'])
def edit_post(post_id):
    '''edit an existing post'''
    report_form = ReportForm()
    post = Post.query.get(post_id)
    if request.method=='POST':
        form = request.form
        if form['title'] and form['tags'] and form['content']:
            post.title = form['title']
            post.content = form['content']
            post.tags = form['tags']
            db.session.commit()
            flash('Update succesful.', 'success')
            return redirect(url_for('post.find_post', post_id=post.id))
        else:
            flash('Please check your input.', 'warning')
            return redirect(url_for('edit_post', post_id=post.id))
    return render_template('editor.html', form=post, report_form=report_form)

