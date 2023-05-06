import unittest
import json
from app import app


class TestParkingAPI(unittest.TestCase):

    # Test / endpoint
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Welcome to parking management'})

    # Test /token endpoint
    def test_get_token(self):
        tester = app.test_client(self)
        response = tester.post('/token', data=json.dumps({'username': 'admin1', 'password': 'passw0rd'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'token', response.data)

    # Test /parking endpoint
    def test_park_vehicle(self):
        tester = app.test_client(self)
        # Set up a valid JWT token
        token_response = tester.post('/token', data=json.dumps({'username': 'admin1', 'password': 'passw0rd'}),
                                     content_type='application/json')
        token = json.loads(token_response.data)['token']
        # Test parking a vehicle
        response = tester.post('/parking', headers={'Authorization': f'Bearer {token}'},
                               data=json.dumps({'vehicle_number': 'ABC-123'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Test /parking/<string:vehicle_number> endpoint
    def test_get_parking_spot(self):
        tester = app.test_client(self)
        # Set up a valid JWT token and park a vehicle
        token_response = tester.post('/token', data=json.dumps({'username': 'admin1', 'password': 'passw0rd'}),
                                     content_type='application/json')
        token = json.loads(token_response.data)['token']
        park_response = tester.post('/parking', headers={'Authorization': f'Bearer {token}'},
                                    data=json.dumps({'vehicle_number': 'ABC-123'}), content_type='application/json')
        # Test retrieving parking spot of the parked vehicle
        response = tester.get('/parking/ABC-123', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)

    # Test /parking/<string:vehicle_number> endpoint for invalid vehicle
    def test_get_parking_spot_invalid(self):
        tester = app.test_client(self)
        # Set up a valid JWT token and park a vehicle
        token_response = tester.post('/token', data=json.dumps({'username': 'admin1', 'password': 'passw0rd'}),
                                     content_type='application/json')
        token = json.loads(token_response.data)['token']
        park_response = tester.post('/parking', headers={'Authorization': f'Bearer {token}'},
                                    data=json.dumps({'vehicle_number': 'ABC-123'}), content_type='application/json')
        # Test retrieving parking spot of an invalid vehicle
        response = tester.get('/parking/XYZ-456', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {'message': 'Vehicle not found in the parking lot.'})


if __name__ == '__main__':
    unittest.main()
