# Description: This file is the initializer of the app package. It imports the routes module that defines the URL routes for the application, and then it creates an application instance.
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes