from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import api.settings as settings

app = Flask(__name__)


@app.get("/")
def home():
    return "This is home page"

if __name__ == '__main__':
    app.run()
