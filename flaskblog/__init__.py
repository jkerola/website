'''main package init'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Config
#routes
from flaskblog.main.routes import main
from flaskblog.post.routes import post

#database
DB = SQLAlchemy()

def create_app(config_class=Config):
    '''creates the app with the given configuration'''
    #app
    app = Flask(__name__)
    app.config.from_object(config_class)

    #extensions
    DB.init_app(app)

    #routes
    app.register_blueprint(main)
    app.register_blueprint(post)

    #errors
    # from flaskblog.errors.handlers import errors
    # app.register_blueprint(errors)
    return app
