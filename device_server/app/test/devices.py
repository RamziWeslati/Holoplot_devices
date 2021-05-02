from app.test.fixtures import app

_base_set = [i for i in range(1000)]

def generate_mock_data(app):
	"""generates test data for device related tests in /device folder
	params:
	- app: pytest fixture: current/generated test app
	returns:
	multiplier_sets: list of sets: a list of sets where each is a set
	 of multiplier per each multiplier in config
	none_multiplier_set: set: a set of multipliers that are not always devided by config multipliers
	"""
	with app.app_context():
		roles_by_multiplier = app.config['ROLES_BY_MULTIPLIER']
		multipliers = list(roles_by_multiplier.keys())
		multiplier_sets = []
		for multipler in multipliers:
			multiplier_sets.append(set(( id_ for id_ in _base_set if id_ % multipler == 0)))

		_none_multiplier_id = next(id_ for id_ in _base_set
			if (id_ != 0) and (id_ not in multipliers))
		none_multiplier_set = set(( id_ for id_ in _base_set if id_ % _none_multiplier_id == 0))

	return multiplier_sets, none_multiplier_set

#Hardcoded
# device_3_ids = set(( i for i in _base_set if i % 3 == 0))
# device_5_ids = set(( i for i in _base_set if i % 5 == 0))
# device_2_ids = set(( i for i in _base_set if i % 2 == 0))
