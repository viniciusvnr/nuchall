from flask import Blueprint
from flask_restful import Api
from resources.Account import *
from resources.Merchant import *
from resources.Authorize import *
from resources.ApiVersion import GetVersion
from resources.Healthcheck import HealthCheck

api_version = 'v1.0'
api_bp_v1 = Blueprint('api', __name__, url_prefix='/api/' + api_version)
api = Api(api_bp_v1)

# Api Routes
api.add_resource(GetVersion, '/version')
api.add_resource(Account, '/account')
api.add_resource(AccountById, '/account/<accountid>')
api.add_resource(GetTransactions, '/account/<accountid>/transaction')
api.add_resource(GetTransactionById, '/account/<accountid>/transaction/<tid>')
api.add_resource(Merchant, '/merchant')
api.add_resource(GetMerchantById, '/merchant/<merchandid>')
api.add_resource(Authorize, '/authorize')
api.add_resource(HealthCheck, '/healthcheck')
