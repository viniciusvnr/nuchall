from flask import request, jsonify
from flask_restful import Resource
from services.TransactionAuthorizationService import authorize_transaction
from marshmallow import Schema, fields


class AccountSchema(Schema):
    cardIsActive = fields.Boolean(required=True)
    limit = fields.Float(required=True)
    denylist = fields.List(fields.String())


class TransactionSchema(Schema):
    merchant = fields.String(required=True)
    amount = fields.Float(required=True)


class AuthorizeSchema(Schema):
    account = fields.Nested(AccountSchema)
    transaction = fields.Nested(TransactionSchema)
    latesttransaction = fields.UUID(fields.String())


class Authorize(Resource):
    def post(self):

        schema = AuthorizeSchema()
        validate = schema.load(request.json)

        if validate.errors:
            return {"error": validate.errors}, 400
        else:
            make_authorization = authorize_transaction()
            return make_authorization, 201
