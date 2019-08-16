from flask import Blueprint
from flask_restful import Api
from controllers.Authorize import Authorize
from controllers.ApiVersion import GetVersion
from controllers.Healthcheck import HealthCheck

api_version = "v1.0"
api_bp_v1 = Blueprint("api", __name__, url_prefix="/api/" + api_version)
api = Api(api_bp_v1)

# Api Routes
api.add_resource(GetVersion, "/")
api.add_resource(Authorize, "/authorize")
api.add_resource(HealthCheck, "/healthcheck")
