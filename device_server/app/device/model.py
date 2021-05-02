from flask import current_app

class Device:
    """the Device class is an abstraction of one device
    Attributes:
    device_id: int
    role: string: role that maps to the device_id, fetched from config
    """
    def __init__(self, id_):
        #store_id
        self.device_id = id_
        #fetch roles and multipliers
        roles_by_multiplier = current_app.config['ROLES_BY_MULTIPLIER']
        role_all_multipliers = current_app.config['ROLE_ALL_MULTIPLIERS']
        role_none_multipliers = current_app.config['ROLE_NONE_MULTIPLIERS']
        n_multipliers = len(roles_by_multiplier)
        _role = []

        #check if id can be map to any role
        for multiplier, role in roles_by_multiplier.items():
            if (id_ % multiplier == 0):
                _role.append(role)

    
        #assign role
        if (len(_role) == 1):           #device was assigned to exactly one role
            self.role = _role[0]
        elif len(_role) == n_multipliers:     #device maps to all roles
            self.role = role_all_multipliers  
        else:                                    #device's role is none existing or ambiguous
            self.role = role_none_multipliers