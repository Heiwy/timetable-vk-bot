from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")

    # Disable logging to stderr
    SQLALCHEMY_ECHO = False

    # Disable monitoring changes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
