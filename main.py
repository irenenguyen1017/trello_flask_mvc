import os

from flask import Flask

from controllers.cards_controller import cards_bp

# from flask_sqlalchemy import SQLAlchemy
from db import db, ma

# from flask_marshmallow import Marshmallow


# db = SQLAlchemy() # moved to db.py
# ma = Marshmallow()


def create_app():  # automatically called if it is named create_app(). Otherwise, it should be explicit in the .flaskenv `FLASK_APP=main:the other name`
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    # db = SQLAlchemy(app)
    db.init_app(app)
    ma.init_app(app)

    # @app.route("/")
    # def index():
    #     return "Hello, world!"

    app.register_blueprint(cards_bp)

    return app
