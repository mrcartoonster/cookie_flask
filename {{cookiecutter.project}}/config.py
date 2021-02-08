# -*- coding: utf-8 -*-
from environs import Env

env = Env()
env.read_env()


class Config:
    """
    Base Flask config.
    """

    SECRET_KEY = env("SECRET_KEY")
    FLASK_APP = env("FLASK_APP")
    FLASK_ENV = env("FLASK_ENV")
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True


class ProdConfig(Config):
    """
    Prouction config for Flask app.
    """

    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    """
    Development config.
    """

    DEBUG = True


class TestingConfig(Config):
    """
    TestingConfig for app.
    """

    TESTING = True
    WTF_CSRF_ENABLED = False
