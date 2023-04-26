# Workshop2023 REST API application

This is a REST API application for car workshop, 
that store data for cars and repairs.
Firebase file storage is used for photos.

## Install
`use:`

    requirements.txt

## Run the app

    set FLASK_APP=./main.py

## Run tests
    pip install pytest
`all tests in test folder`

# REST API

The REST API is described below:

## Register user:
### Request
`POST /register`

    http://127.0.0.1:5000/register
### Response
    200 OK
    "token": "generated_token"
 ## Login user:
### Request
`POST /login`

    http://127.0.0.1:5000/login
### Response
    200 OK
    "token": "generated_token"
## Add car to database:
### Request
`POST /cars`

    http://127.0.0.1:5000/cars
### Response
    201 CREATED
    {
    "car_brand": "Car Brand",
    "year": Year,
    "id": id,
    "created_at": "date_created",
    "car_model": "Car Model",
    "VIN": "VIN number"
    }
## Get all cars from database:
### Request
`GET /cars`

    http://127.0.0.1:5000/cars
### Response
    200 OK
    List of all cars in database
## Get a single car from database:
### Request
`GET /car/id`

    http://127.0.0.1:5000/car/id
### Response
    200 OK
    {
    "car_brand": "Car Brand",
    "year": Year,
    "id": id,
    "created_at": "date_created",
    "car_model": "Car Model",
    "VIN": "VIN number"
    }
## Edit car:
### Request
`PUT /car/id`

    http://127.0.0.1:5000/car/id
### Response
    200 OK
    {
    "car_brand": "Car Brand",
    "year": Year,
    "id": id,
    "created_at": "date_created",
    "car_model": "Car Model",
    "VIN": "VIN number"
    }
## Post a repair:
### Request
`POST /repairs`

    http://127.0.0.1:5000/repairs
### Response
    200 OK
    {
    "receipt_photo": "https://some_url.com",
    "created_at": "date_created",
    "VIN": "VIN number",
    "description": "Description",
    "car_id": car_id,
    "mileage": Mileage,
    "amount": Amount,
    "user_id": user_id,
    "id": id
    }
## Get repairs:
### Request
`GET /repairs`

    http://127.0.0.1:5000/repairs
### Response
    200 OK
    List of repairs depending on user role
## Get single repair:
### Request
`GET /repair/id`

    http://127.0.0.1:5000/repair/id
### Response
    200 OK
    {
    "receipt_photo": "https://some_url.com",
    "created_at": "date_created",
    "VIN": "VIN number",
    "description": "Description",
    "car_id": car_id,
    "mileage": Mileage,
    "amount": Amount,
    "user_id": user_id,
    "id": id
    }
## Delete repair:
### Request
`DELETE /repair/id`

    http://127.0.0.1:5000/repair/id
### Response
    204 NO CONTENT
## Edit repair:
### Request
`PUT /repair/id`

    http://127.0.0.1:5000/repair/id
### Response
    200 OK
    {
    "receipt_photo": "https://some_url.com",
    "created_at": "date_created",
    "VIN": "VIN number",
    "description": "Description",
    "car_id": car_id,
    "mileage": Mileage,
    "amount": Amount,
    "user_id": user_id,
    "id": id
    }