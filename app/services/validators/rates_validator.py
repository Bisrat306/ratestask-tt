from marshmallow import Schema, fields, validates, ValidationError
from datetime import datetime

class AveragePricesSchema(Schema):
    ''' Validates inputs for the get_average_prices function'''
    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    origin = fields.String(required=True)
    destination = fields.String(required=True)
