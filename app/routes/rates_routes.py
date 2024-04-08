from flask_restx import Namespace, Resource, Api
from flask import request,jsonify
from marshmallow import ValidationError

from app.services.validators.rates_validator import AveragePricesSchema
from app.services.rates_service import RatesService

api = Api()
rates_ns = Namespace('rates', description='Rates operations')
rates_service = RatesService() # Instantiate Rates service provider



@rates_ns.route('/')
class AveragePrices(Resource):
    @api.doc(params={
        'date_from': {'description': 'Start date in YYYY-MM-DD format', 'required': True},
        'date_to': {'description': 'End date in YYYY-MM-DD format', 'required': True},
        'origin': {'description': 'Origin port code or region slug', 'required': True},
        'destination': {'description': 'Destination port code or region slug', 'required': True}
    })
    def get(self):

        try:
            # Validate input
            schema = AveragePricesSchema()
            params = schema.load(request.args)
        except ValidationError as err:
            return {'error': err.messages}, 400
        

        date_from = params['date_from']
        date_to = params['date_to']
        origin = params['origin']
        destination = params['destination']

       # Call the service method to get the average prices
        average_prices = rates_service.get_average_prices(date_from, date_to, origin, destination)
        
        return jsonify(average_prices)