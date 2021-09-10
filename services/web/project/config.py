
"""Flask configuration variables."""
import os


basedir = os.path.abspath(os.path.dirname(__file__))
os.getenv(os.path.join(basedir, ".env.dev"))


class Config(object):
    """Set Flask configuration from .env file."""
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # General Config
    TEMPLATE_FOLDER = f"{os.getenv('APP_FOLDER')}/project/template"

    # SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")





