# ParkingLot

Build docker image fist by using the command:
docker build -t <desired_image_name> .

then run the docker image by:
docker run --name=<desire_container_name> -d -p 8080:8080 <previously_given_image_name>

then open postman and APIs can be tested from there.
------------------------------------------------------------------------------

API documentation:
(you can copy paste this cURL commands into postman, or run them from terminal)
Note: change the variable parameters for your system

1. Get token to verify yourself.

curl --location 'http://localhost:8080/token' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin1",
    "password": "passw0rd"
}
'


2. Alot a parking space for the vehicle


curl --location 'http://localhost:8080/parking' \
--header 'Authorization: something eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluMSJ9.rIZLWEuYReTb2PJ7lUaBGZx0eZsTvChNDYG7oNrkZjQ' \
--header 'Content-Type: application/json' \
--data '{
    "vehicle_number": "ABC212"
}'

3. Get Parking spot for a given vehicle

curl --location 'http://localhost:8080/parking/ABC212' \
--header 'Authorization: something eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluMSJ9.rIZLWEuYReTb2PJ7lUaBGZx0eZsTvChNDYG7oNrkZjQ' \
--data ''

------------------------------------------------------------------------------

Future Scope:

1) Free up parking space

2) Validate vehicle number

3) Better token management

