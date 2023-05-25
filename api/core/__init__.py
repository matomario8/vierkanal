from flask import Flask
from . import api_handler

def create_app():

    app = Flask("core")

    app.register_blueprint(api_handler.imgboard)

    return app

