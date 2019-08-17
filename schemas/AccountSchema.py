from marshmallow import Schema, fields


class AccountSchema(Schema):
    cardIsActive = fields.Boolean(required=True)
    limit = fields.Float(required=True)
    denylist = fields.List(fields.String())
