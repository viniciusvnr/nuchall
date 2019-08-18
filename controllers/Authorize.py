from flask import request
from flask_restful import Resource
from schemas.AuthorizeSchema import AuthorizeSchema
from services.TransactionAuthorizationService import authorize_transaction


class Authorize(Resource):
    def post(self):

        schema = AuthorizeSchema()
        input_object = schema.load(request.json)

        if input_object.errors:
            return input_object.errors, 400
        else:
            do_authorization = authorize_transaction(input_object.data)
            return do_authorization, 200
