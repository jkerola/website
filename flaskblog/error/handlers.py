from flask import Blueprint, render_template
from flaskblog.main.forms import ReportForm

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    '''404 error handler'''
    report_form = ReportForm()
    return render_template('errors/404.html', report_form=report_form), 404

@errors.app_errorhandler(403)
def error_403(error):
    '''403 error handler'''
    report_form = ReportForm()
    return render_template('errors/403.html', report_form=report_form), 403
    
@errors.app_errorhandler(500)
def error_500(error):
    '''500 error handler'''
    report_form = ReportForm()
    return render_template('errors/500.html', report_form=report_form), 500

