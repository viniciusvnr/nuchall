from flask import request
from flask_restful import Resource
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
            # TODO: chamada para o serviço de authorização
            return {"message": "schema validated"}, 201
