from marshmallow import Schema, fields
from schemas.AccountSchema import AccountSchema
from schemas.TransactionSchema import TransactionSchema


class AuthorizeSchema(Schema):
    account = fields.Nested(AccountSchema, required=True)
    transaction = fields.Nested(TransactionSchema, required=True)
    latesttransactions = fields.List(fields.Nested(TransactionSchema), required=True)
