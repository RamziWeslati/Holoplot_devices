from flask import request, jsonify
from flask_accepts import accepts, responds #TODO make use of accepts and schema
from flask_restx import Namespace, Resource
from flask.wrappers import Response

from .service import DeviceService

api = Namespace("device", description="device description to do") #TODO change this to have meaningful desc

@api.route("/<int:device_id>")
@api.param("deviceId", "device map by ID")
class deviceMapping(Resource):
    # @responds()
    def get(self, device_id: int) -> Response:
        """Get device groupe"""

        role = DeviceService.get_role(device_id)
        return jsonify(dict(status="Success", role=role))