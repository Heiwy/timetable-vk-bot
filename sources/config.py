from os import environ


class Config:
    SQLALCHEMY_DATABASE_URL = environ.get("SQLALCHEMY_DATABASE_URL")

    # Disable logging to stderr
    SQLALCHEMY_ECHO = False

    # Disable monitoring changes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
