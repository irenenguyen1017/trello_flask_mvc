import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(): #automatically called if it is named create_app(). Otherwise, it should be explicit in the .flaskenv `FLASK_APP=main:the other name`
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    
    db = SQLAlchemy(app)
    
    @app.route("/")
    def index():
        return "Hello, world!"
    
    return app