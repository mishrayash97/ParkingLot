from flask import Flask, jsonify, request
import jwt
from utils import authenticate_token
from data_access import parking_lot, LEVEL_A_SPOTS, LEVEL_B_SPOTS, level


app = Flask(__name__)

# secret key for JWT authentication.
JWT_SECRET = 'mysecret'

# Authenticate user and generate a JWT token.
@app.route('/token', methods=['POST'])
def get_token():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Authenticate the user.
    if username == 'admin' and password == 'password':
        token = jwt.encode({'username': username}, JWT_SECRET, algorithm='HS256')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401

# Automatically assign a parking spot to a new vehicle.
@app.route('/parking', methods=['POST'])
@authenticate_token
def park_vehicle():
    data = request.get_json()
    vehicle_number = data['vehicle_number']

    # Check if a parking spot is available.
    if level =='A':
        if(len(LEVEL_A_SPOTS)<20):
            spot = LEVEL_A_SPOTS.pop(0)
            level = 'B'
        elif(len(LEVEL_B_SPOTS)<20):
            spot = LEVEL_B_SPOTS.pop(0)
            level = 'A'
        else:
            return jsonify({'message': 'Parking lot is full.'}), 400
    else:
        if(len(LEVEL_B_SPOTS)<20):
            spot = LEVEL_B_SPOTS.pop(0)
            level = 'A'
        elif(len(LEVEL_A_SPOTS)<20):
            spot = LEVEL_A_SPOTS.pop(0)
            level = 'B'
        else:
            return jsonify({'message': 'Parking lot is full.'}), 400

    # Store the vehicle data in the parking lot dictionary.
    parking_lot[vehicle_number] = {'level': level, 'spot': spot}

    return jsonify({'level': level, 'spot': spot}), 200

# Retrieve the parking spot number of a particular vehicle.
@app.route('/parking/<string:vehicle_number>', methods=['GET'])
@authenticate_token
def get_parking_spot(vehicle_number):
    if vehicle_number in parking_lot:
        level = parking_lot[vehicle_number]['level']
        spot = parking_lot[vehicle_number]['spot']
        return jsonify({'level': level, 'spot': spot}), 200
    else:
        return jsonify({'message': 'Vehicle not found in the parking lot.'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)
