from flask_restx import Api
from .routes.rates_routes import rates_ns

def init_ns(app):
    '''
    Registers all namespaces in the app
    '''
    api = Api(
        app,
        title='Rates Api',
        description='This a Rates Task api.'
        )
    
    api.add_namespace(rates_ns, path='/rates')
