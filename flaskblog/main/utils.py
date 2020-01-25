'''Utility functions for the main package [email].'''
from flaskblog import mail
from flask_mail import Message
from flaskblog import Config


def send_report_notification(title, content, email, date):
    '''Sends an email about the report to administration.'''
    sender = Config._CUSTOM_SENDER
    recipient = Config._CUSTOM_RECIPIENT
    recipient_2 = Config._CUSTOM_ARCHIVE
    msg = Message('Issue Report',
               sender=sender,
               recipients=[recipient, recipient_2])
    msg.body = f'''A new issue has been report at jkerola.com:

'{date}, by {email}'
-----------------
'{title}',
'{content}'
-----------------

Please check on the issue ASAP.'''
    mail.send(msg)

def send_contact_notification(name, title, email, content):
    '''Sends an email to me when the contact form is used.'''
    sender = Config._CUSTOM_SENDER
    recipient = Config._CUSTOM_RECIPIENT
    recipient_2 = Config._CUSTOM_ARCHIVE
    msg = Message('New Contact', 
                sender=sender, 
                recipients=[recipient, recipient_2])
    msg.body = f'''{name} at {email}:
------------------
{title}
{content}
------------------
end message'''
    mail.send(msg)
    