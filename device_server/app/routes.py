def register_routes(api, app, root="api"):
	from app.device import register_routes as attach_device

	#Add routes
	attach_device(api, app)