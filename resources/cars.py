from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.cars_manager import CarsManager
from models import RoleType
from schemas.request_schemas.cars import CarsRequestSchema
from schemas.response_schemas.cars import CarsResponseSchema
from utils.decorators import validate_schema, permission_required


class CarsResource(Resource):
    @auth.login_required()
    @validate_schema(CarsRequestSchema)
    def post(self):
        data = request.get_json()
        car = CarsManager.create_car(data)
        return CarsResponseSchema().dump(car), 201

    @auth.login_required()
    def get(self):
        cars = CarsManager.get_all_cars()
        return CarsResponseSchema().dump(cars, many=True)


class CarResource(Resource):
    @auth.login_required()
    def get(self, pk):
        car = CarsManager.get_single_car(pk)
        return CarsResponseSchema().dump(car)

    @auth.login_required()
    @permission_required([RoleType.supervisor, RoleType.admin])
    @validate_schema(CarsRequestSchema)
    def put(self, pk):
        data = request.get_json()
        CarsManager.update_car(data, pk)
        updated_car = CarsManager.get_single_car(pk)
        return CarsResponseSchema().dump(updated_car)
