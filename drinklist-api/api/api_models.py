"""
Module containing models for whole API to use.
"""

from flask_restplus import fields
from . import API
from ..db_models import STD_STRING_SIZE

ROOT_MODEL = API.model('RootModel', {
    'beverages': fields.Url('api.beverages_beverage_list'),
    'users': fields.Url('api.users_user_list'),
    'history': fields.Url('api.history_history_resource'),
})


BEVERAGE_POST = API.model('BeveragePOST', {
    'name': fields.String(max_length=STD_STRING_SIZE, title='Name'),
    'price': fields.Integer(title='Price'),
    'stock': fields.Integer(title='Stock'),
})


BEVERAGE_GET = API.inherit('BeverageGET', BEVERAGE_POST, {
    'id': fields.Integer(min=1, example=1, readonly=True, title='Internal Identifier'),
})

USER_PUT = API.model('UserPUT', {
    'active': fields.Boolean(title='Active'),
})

USER_GET = API.inherit('UserGET', USER_PUT, {
    'name': fields.String(max_length=STD_STRING_SIZE, title='Name'),
    'id': fields.Integer(min=1, example=1, readonly=True, title='Internal Identifier'),
    'balance': fields.Integer(title='Balance'),
})

TRANSACTION_BEVERAGE_GET = API.model('TransactionBeverageGET', {
    'beverage': fields.Nested(BEVERAGE_GET),
    'count': fields.Integer(min=1, example=1, title='Count of beverages'),
    'price': fields.Float(title='Price of beverage'),
})

TRANSACTION_GET = API.model('TransactionGET', {
    'user': fields.Nested(USER_GET),
    'beverages': fields.List(fields.Nested(TRANSACTION_BEVERAGE_GET), attribute="_beverages"),
    'amount': fields.Integer(),
    'balance': fields.Integer(),
    'reason': fields.String(),
    'cancels-id': fields.Integer(),
    'timestamp': fields.DateTime(),
})