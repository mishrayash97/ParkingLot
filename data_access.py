#In memory json object that stores all parking data
parking_lot = {}

# Level A has parking spots numbered from 1 to 20, and Level B has parking spots numbered from 21 to 40.
LEVEL_A_SPOTS = list(range(1, 21))
LEVEL_B_SPOTS = list(range(21, 41))

# secret key for JWT authentication.
JWT_SECRET = 'mysecret'