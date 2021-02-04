# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

csrf_protection = CSRFProtect()


def create_app():
    app = Flask(__name__)

    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    register_blueprints(app)
    register_error_pages(app)
    return app


def register_blueprints(app):
    """
    Adding blueprints.
    """
    # from .contact.contact import contact_blueprint

    # app.register_blueprint(contact_blueprint)


def initialize_extensions(app):
    """
    Add your flask extensions.
    """

    csrf_protection.init_app(app)


def register_error_pages(app):
    """
    Base error pages.
    """

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404
