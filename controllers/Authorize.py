from flask import request, current_app
from flask_restful import Resource
from schemas.AuthorizeSchema import AuthorizeSchema
from services.TransactionAuthorizationService import authorize_transaction


class Transaction:
    def __init__(self, request_input):
        self.request_input = request_input

        self.card_is_active = request_input["account"]["cardIsActive"]
        self.account_limit = request_input["account"]["limit"]
        self.deny_list = request_input["account"]["denylist"]
        self.last_transactions = request_input["lasttransactions"]
        self.merchant = request_input["transaction"]["merchant"]
        self.amount = request_input["transaction"]["amount"]
        self.time = request_input["transaction"]["time"]


class Authorize(Resource):
    def post(self):
        schema = AuthorizeSchema()
        # Valida o schema
        input_object = schema.load(request.json)
        if input_object.errors:
            current_app.logger.warning(str(input_object.errors))
            return input_object.errors, 400

        transaction_object = Transaction(input_object.data)
        try:
            do_authorization = authorize_transaction(transaction_object)
        except Exception as e:
            current_app.logger.info(str(e))
        else:
            return do_authorization, 200
