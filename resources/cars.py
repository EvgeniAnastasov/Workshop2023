from flask import request
from flask_restful import Resource

from managers.cars_manager import CarsManager
from schemas.request_schemas.cars import CarsRequestSchema
from schemas.response_schemas.cars import CarsResponseSchema
from utils.decorators import validate_schema


class CarsResource(Resource):
    @validate_schema(CarsRequestSchema)
    def post(self):
        data = request.get_json()
        car = CarsManager.create_car(data)
        return CarsResponseSchema().dump(car), 201
