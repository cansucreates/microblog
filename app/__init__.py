# Description: This file is the initializer of the app package. It imports the routes module that defines the URL routes for the application, and then it creates an application instance.
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# `from app import routes, models` is importing the `routes` and `models` modules from the `app`
# package. This allows the application to access the URL routes defined in the `routes` module and the
# database models defined in the `models` module.
from app import routes, models