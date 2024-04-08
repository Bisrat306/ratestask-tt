import unittest
from flask import url_for
from app.routes.rates_routes import rates_ns
from app import create_app

class TestRatesRoutes(unittest.TestCase):
    def setUp(self):
        # Get the existing Flask app instance
        self.app = create_app('test')
        self.client = self.app.test_client()

    def test_get_average_prices(self):
        # Make a GET request to the /rates endpoint with valid parameters
        response = self.client.get('/rates/?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains JSON data
        self.assertTrue(response.is_json)

        # Check if the response contains the expected keys
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_empty_origin(self):
        # Make a GET request with an empty origin
        response = self.client.get('/rates/?date_from=2016-01-01&date_to=2016-01-10&destination=north_europe_main')

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

    def test_empty_destination(self):
        # Make a GET request with an empty destination
        response = self.client.get('/rates/?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH')

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_dates(self):
        # Make a GET request with invalid dates
        response = self.client.get('/rates/?date_from=2016-01-33&date_to=2026-01-31&origin=CNSGH&destination=north_europe_main')

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
