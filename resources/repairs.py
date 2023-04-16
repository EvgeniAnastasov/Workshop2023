from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.repairs_manager import RepairManager
from schemas.request_schemas.repairs import RepairRequestSchema
from schemas.response_schemas.repairs import RepairsResponseSchema
from utils.decorators import validate_schema


class RepairsResource(Resource):
    @auth.login_required()
    @validate_schema(RepairRequestSchema)
    def post(self):
        data = request.get_json()
        repair = RepairManager.create_repair(data)

        return RepairsResponseSchema().dump(repair)
