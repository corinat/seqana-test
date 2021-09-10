import os
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for
)
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error
from requests import Response
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine
from flask import Flask, render_template
import json


app = Flask(__name__, template_folder='template')
app.config.from_object("project.config.Config")
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)

# cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class ConnectPostgres:
    @staticmethod
    def connect_postgres():
        db_string = create_engine(os.getenv("DATABASE_URL", "sqlite://"))
        conn = db_string.raw_connection()
        db = scoped_session(sessionmaker(bind=db_string))
        cur = conn.cursor()
        return conn, cur


@app.route("/template/<path:filename>")
def template(filename):
    return send_from_directory(app.config["TEMPLATE_FOLDER"], filename)



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")