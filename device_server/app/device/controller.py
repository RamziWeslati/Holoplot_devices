from flask import request, jsonify
from flask_restx import Namespace, Resource
from flask.wrappers import Response

from .service import DeviceService

api = Namespace("device", description="device description to do") #TODO change this to have meaningful desc

@api.route("/<int:device_id>")
@api.param("device_id", "device map by ID")
class deviceMapping(Resource):
    def get(self, device_id: int) -> Response:
        """Get device role given device id"""
        role = DeviceService.get_role(device_id)
        return jsonify(dict(status="Success", role=role))