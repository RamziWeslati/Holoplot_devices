BASE_ROUTE = "device"

def register_routes(api, app, root="api"):
	from .controller import api as device_api
	api.add_namespace(device_api, path=f"/{root}/{BASE_ROUTE}")