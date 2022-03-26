from flask import Flask, Blueprint
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity

import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.exceptions import Unauthorized
from configs.config import DevelopmentConfig


app = Flask(__name__)

blueprint = Blueprint("api",__name__,url_prefix="/api")

authorizations = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Type in the *value into the box below**Bearer & where jwt is token",
    }
}

# calling configs
app.config.from_object(DevelopmentConfig)

api = Api(
    blueprint,doc="/doc",
    
    # to turn documentation off set doc=Flase
    authorizations=authorizations,
    title="Task management api",
    description="task manager api",
    version="1.0",
    author="Giche",
)
app.register_blueprint(blueprint)
# importing error handlers
from error_handler import handler


jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# importing db models
from models.usermodel import Users_model
from models.taskmodel import Task_model


@app.before_first_request
def create():
    db.create_all()


from resources.tasks import *
from resources.user import *
from resources.authentication import *

# @app.route('/debug-sentry')
# def trigger_error():
#     division_by_zero = 1 / 0

if __name__ == "__main__":
    app.run()
