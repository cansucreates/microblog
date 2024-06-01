# Description: This file is the initializer of the app package. It imports the routes module that defines the URL routes for the application, and then it creates an application instance.
from flask import Flask

app = Flask(__name__)

from app import routes