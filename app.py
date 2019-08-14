from flask import Blueprint
from flask_restful import Api
from resources.Account import *
from resources.Merchant import *
from resources.Authorize import *
from resources.ApiVersion import GetVersion
from resources.healthcheck import HealthCheck


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(GetVersion, '/version')
api.add_resource(Account, '/account')
api.add_resource(AccountById, '/account/<accountid>')
api.add_resource(GetTransactions, '/account/<accountid>/transaction')
api.add_resource(GetTransactionById, '/account/<accountid>/transaction/<tid>')
api.add_resource(Merchant, '/merchant')
api.add_resource(GetMerchantById, '/merchant/<merchandid>')
api.add_resource(Authorize, '/authorize')
api.add_resource(HealthCheck, '/healthcheck')



