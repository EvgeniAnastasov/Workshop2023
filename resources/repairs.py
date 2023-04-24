from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.repairs_manager import RepairManager
from models import RoleType
from schemas.request_schemas.repairs import RepairRequestSchema
from schemas.response_schemas.repairs import RepairResponseSchema
from utils.decorators import validate_schema, permission_required


class RepairsResource(Resource):
    @auth.login_required()
    @validate_schema(RepairRequestSchema)
    def post(self):
        data = request.get_json()
        repair = RepairManager.create_repair(data)

        return RepairResponseSchema().dump(repair), 201

    @auth.login_required()
    def get(self):
        repairs = RepairManager.get_repairs()
        return RepairResponseSchema().dump(repairs, many=True)


class RepairResource(Resource):
    @auth.login_required()
    @permission_required([RoleType.supervisor, RoleType.admin])
    def get(self, pk):
        repair = RepairManager.get_single_repair(pk)
        return RepairResponseSchema().dump(repair)

    @auth.login_required()
    @permission_required([RoleType.supervisor, RoleType.admin])
    @validate_schema(RepairRequestSchema)
    def put(self, pk):
        data = request.get_json()
        RepairManager.update_repair(data, pk)
        updated_repair = RepairManager.get_single_repair(pk)
        return RepairResponseSchema().dump(updated_repair)

    @auth.login_required()
    @permission_required([RoleType.admin])
    def delete(self, pk):
        RepairManager.delete_repair(pk)
        return "", 204
