class Device:
	def __init__(self, id):
		_role = ''
		if (id % 3 == 0):
			_role += 'Bing'
		if (id % 5 == 0):
			_role += 'Bang'
    
		#assign role
		if ( _role in ['Bing', 'Bang']):
			self.role = _role
		else:
			self.role = 'Boom' if _role else 'Meh'
