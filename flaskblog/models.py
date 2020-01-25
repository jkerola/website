'''database models module'''
from datetime import datetime
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    '''Main blogger'''
    #attributes
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    real_name = db.Column(db.String(128), nullable=False)
    email_personal = db.Column(db.String(128), nullable=False)
    email_company = db.Column(db.String(128), nullable=False)
    profile_img = db.Column(db.String(32), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)

    #relationships
    posts = db.relationship('Post', backref='author', lazy=True)

    #methods
    #this is for resetting the password, copied from a tutorial project
    #thank you to Corey Schafer at coreyMS.com for his excellent tutorials on Flask!
    def get_reset_token(self, expires_in=1800):
        '''Creates a token with user.id payload that expires in 30 minutes'''
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return serializer.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        '''Verifys that the token is within time limit, returns user.id payload'''
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = serializer.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def get_name(self):
        '''return real name for blog titles'''
        return self.real_name

    def __repr__(self):
        '''self-representation method'''
        return f"User({self.username}, {self.email_company}, {self.profile_img})"


class Report(db.Model):
    '''Website issue reports made by readers'''
    #attributes
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        '''self-representation method'''
        return f"Report {self.id}: {self.date_posted} {self.title}"

class Post(db.Model):
    '''Blog posts'''
    #attributes
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.String(20000), nullable=False)
    tags = db.Column(db.String(256), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    #relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        
    def __repr__(self):
        return f"Post {self.id}:({self.date_posted} {self.title})"



