from flask import request
from flask_restful import Resource

from managers.cars_manager import CarsManager
from schemas.request_schemas.cars import CarsRequestSchema
from utils.decorators import validate_schema


class CarsResource(Resource):
    @validate_schema(CarsRequestSchema)
    def post(self):
        data = request.get_json()
        CarsManager.create_car(data)
