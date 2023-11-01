from flask_restx import fields
from app import rest_api

user_model = rest_api.model('User', {
    "username": fields.Integer,
    "password": fields.String,

})