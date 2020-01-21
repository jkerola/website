'''main package init'''
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_blogging import BloggingEngine, SQLAStorage
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flaskblog.config import Config
from sqlalchemy import create_engine, MetaData

#database
db = SQLAlchemy()
#flask-bloggging
engine = create_engine('sqlite:///flaskblog/blog.db')
blogging_engine = BloggingEngine()
meta = MetaData()
storage= SQLAStorage(engine, metadata=meta)
meta.create_all(bind=engine)
#csfr
csfr = CSRFProtect()

#Bcrypt
bcrypt = Bcrypt()

#Login manager
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    '''creates the app with the given configuration'''
    #app
    app = Flask(__name__)
    app.config.from_object(config_class)

    #extensions
    db.init_app(app)
    csfr.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    

    #create blogging engine
    blogging_engine.init_app(app, storage)

    #routes
    #user needs to be placed here to avoid import loops
    #rest are here for consistency
    from flaskblog.blog.routes import blog
    from flaskblog.main.routes import main
    from flaskblog.post.routes import post
    from flaskblog.user.routes import user

    app.register_blueprint(blog)
    app.register_blueprint(main)
    app.register_blueprint(post)
    app.register_blueprint(user)

    #errors
    # from flaskblog.errors.handlers import errors
    # app.register_blueprint(errors)
    return app
