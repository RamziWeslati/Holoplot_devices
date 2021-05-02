from app.test.fixtures import app
from app.test.devices import generate_mock_data
# from app.test.devices import device_3_ids, device_5_ids, device_2_ids   #Hardcoded multipliers

from .service import DeviceService

def test_device_roles(app):
    with app.app_context():
        #import app config
        roles_by_multiplier = app.config['ROLES_BY_MULTIPLIER']
        role_all_multipliers = app.config['ROLE_ALL_MULTIPLIERS']
        role_none_multipliers = app.config['ROLE_NONE_MULTIPLIERS']
        expected_roles = list(roles_by_multiplier.values())
        n_multipliers = len(roles_by_multiplier)
        #generate test data
        device_multiplier_ids, device_none_multiplier_ids = generate_mock_data(app)
        results_one_multiplier_only= []

        #get role for ids that can be devided by EACH multiplier set
        for i in range(n_multipliers):
            if (i == n_multipliers):
                current_mult = i
                next_mult = 0
            else:
                current_mult = i
                next_mult = i + 1
            results_one_multiplier_only.append(map(
                                lambda id_: DeviceService.get_role(id_),
                                device_multiplier_ids[current_mult].difference(
                                    *(device_multiplier_ids[:current_mult] + device_multiplier_ids[next_mult:]))))

        #get role for ids that can be devided by ALL multipliers
        device_all_multipliers = map(
                lambda id_: DeviceService.get_role(id_),
                set.intersection(*device_multiplier_ids))

        #get role for ids that can be devided by NO multipliers
        device_none_multipliers = map(
                lambda id_: DeviceService.get_role(id_),
                device_none_multiplier_ids)

        #compare actual results against expected results
        for mult_index, result_roles in enumerate(results_one_multiplier_only):
            assert all( role == expected_roles[mult_index] for role in result_roles)
        assert all( role == role_all_multipliers for role in device_all_multipliers)
        assert any( role == role_none_multipliers for role in device_none_multipliers)


        """Hardcoded version
            device_3_only_roles = list(map(
                lambda id_: DeviceService.get_role(id_),
                device_3_ids.difference(device_5_ids)))
            device_5_only_roles = map(
                lambda id_: DeviceService.get_role(id_),
                device_5_ids.difference(device_3_ids))
            device_3_5_roles = map(
                lambda id_: DeviceService.get_role(id_),
                device_5_ids.intersection(device_3_ids))
            device_2_roles = map(
                lambda id_: DeviceService.get_role(id_),
                device_2_ids)

        assert all( role == 'Bing' for role in device_3_only_roles)
        assert all( role == 'Bang' for role in device_5_only_roles)
        assert all( role == 'Boom' for role in device_3_5_roles)
        assert any( role == 'Meh' for role in device_2_roles)
        """