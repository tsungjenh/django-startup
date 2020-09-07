from marshmallow import Schema, fields


class UserLoginForm(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)


class UserRegisterForm(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)


class ResetUserPasswordForm(Schema):
    user_id = fields.String(required=True)
