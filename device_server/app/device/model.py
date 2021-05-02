from flask import current_app

class Device:
    def __init__(self, id):
        roles_by_multiplier = current_app.config['ROLES_BY_MULTIPLIER']
        role_all_multipliers = current_app.config['ROLE_ALL_MULTIPLIERS']
        role_none_multipliers = current_app.config['ROLE_NONE_MULTIPLIERS']
        _role = ''
        for multiplier, role in roles_by_multiplier.items():
            if (id % multiplier == 0):
                _role += role

    
        #assign role
        if ( _role in roles_by_multiplier.values()):
            self.role = _role
        else:
            self.role = role_all_multipliers if _role else role_none_multipliers