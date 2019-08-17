from marshmallow import Schema, fields
from schemas.AccountSchema import AccountSchema
from schemas.TransactionSchema import TransactionSchema


class AuthorizeSchema(Schema):
    account = fields.Nested(AccountSchema)
    transaction = fields.Nested(TransactionSchema)
    latesttransaction = fields.UUID(fields.String())
