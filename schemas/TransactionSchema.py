from marshmallow import Schema, fields


class TransactionSchema(Schema):
    merchant = fields.String(required=True)
    amount = fields.Float(required=True)
    time = fields.DateTime(required=True)

