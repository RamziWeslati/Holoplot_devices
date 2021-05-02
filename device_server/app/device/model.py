from flask import current_app

class Device:
    def __init__(self, id):
        roles_by_multiplier = current_app.config['ROLES_BY_MULTIPLIER']
        role_all_multipliers = current_app.config['ROLE_ALL_MULTIPLIERS']
        role_none_multipliers = current_app.config['ROLE_NONE_MULTIPLIERS']
        n_multipliers = len(roles_by_multiplier)
        _role = []
        for multiplier, role in roles_by_multiplier.items():
            if (id % multiplier == 0):
                _role.append(role)

    
        #assign role
        if (len(_role) == 1):
            self.role = _role[0]
        else:
            self.role = role_all_multipliers if len(_role) == n_multipliers else role_none_multipliers