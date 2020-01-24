'''main package init'''
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flaskblog.config import Config

#database
db = SQLAlchemy()

#csfr
csfr = CSRFProtect()

#Bcrypt
bcrypt = Bcrypt()

#Login manager
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

#Mail
mail = Mail()

def create_app(config_class=Config):
    '''creates the app with the given configuration'''
    #app
    app = Flask(__name__)
    app.config.from_object(Config)

    #extensions
    db.init_app(app)
    csfr.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
 
    #routes
    #user needs to be placed here to avoid import loops
    #rest are here for consistency
    from flaskblog.main.routes import main
    from flaskblog.post.routes import post
    from flaskblog.user.routes import user

    app.register_blueprint(main)
    app.register_blueprint(post)
    app.register_blueprint(user)

    #errors
    # from flaskblog.errors.handlers import errors
    # app.register_blueprint(errors)
    return app
