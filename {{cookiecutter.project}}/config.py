# -*- coding: utf-8 -*-
from environs import Env

env = Env()
env.read_env()


class Config:

    SECRET_KEY = env("SECRET_KEY")
    FLASK_APP = env("FLASK_APP")
    FLASK_ENV = env("FLASK_ENV")
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True


class ProdConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
