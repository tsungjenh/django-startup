from marshmallow import Schema, fields


class Echo(Schema):
    echo = fields.String(required=True)
