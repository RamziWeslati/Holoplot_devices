from flask.testing import FlaskClient

from app.test.fixtures import client, app
from app.test.devices import generate_mock_data

# from app.test.devices import device_3_ids, device_5_ids, device_2_ids #Hardcoded version

def test_get_role(app, client: FlaskClient):
    with app.app_context():
        #import app config
        roles_by_multiplier = app.config['ROLES_BY_MULTIPLIER']
        role_all_multipliers = app.config['ROLE_ALL_MULTIPLIERS']
        role_none_multipliers = app.config['ROLE_NONE_MULTIPLIERS']
        expected_roles = list(roles_by_multiplier.values())
        n_multipliers = len(roles_by_multiplier)
        #generate test data
        device_multiplier_ids, device_none_multiplier_ids = generate_mock_data(app)
        results_one_multiplier_only = [] #list of lists
        results_all_multiplier = []
        results_none_multiplier = []

        for i in range(n_multipliers):
            if (i == n_multipliers):
                current_mult = i
                next_mult = 0
            else:
                current_mult = i
                next_mult = i + 1
            set_to_test = device_multiplier_ids[current_mult].difference(
                                    *(device_multiplier_ids[:current_mult] + device_multiplier_ids[next_mult:]))
            _responses = []
            for device_id in set_to_test:
                with client:
                    _responses.append(
                        client.get(
                        f"/api/device/{device_id}",
                        follow_redirects=False).get_json())
            results_one_multiplier_only.append(_responses)

        for device_id in set.intersection(*device_multiplier_ids):
            with client:
                    results_all_multiplier.append(
                        client.get(
                        f"/api/device/{device_id}",
                        follow_redirects=False).get_json())

        for device_id in device_none_multiplier_ids:
            with client:
                    results_none_multiplier.append(
                        client.get(
                        f"/api/device/{device_id}",
                        follow_redirects=False).get_json())

        #evaluate results
        for mult_index, result_roles in enumerate(results_one_multiplier_only):
            assert all( result['role'] == expected_roles[mult_index] for result in result_roles)
        assert all( result['role'] == role_all_multipliers for result in results_all_multiplier)
        assert any( result['role'] == role_none_multipliers for result in results_none_multiplier)





        # expected_only_3_role = 'Bing'
        # expected_only_5_role = 'Bang'
        # expected_3_5_role = 'Boom'
        # expected_some_2_role = 'Meh'

        # results_only_3, results_only_5, results_3_5, results_some_2 = ([] for _ in range(4))

        # for device_id in device_3_ids.difference(device_5_ids):
                # with client:
                #     results_only_3.append(
                #         client.get(
                #         f"/api/device/{device_id}",
                #         follow_redirects=False).get_json())
        # for device_id in device_5_ids.difference(device_3_ids):
           #      with client:
           #          results_only_5.append(
           #              client.get(
           #              f"/api/device/{device_id}",
           #              follow_redirects=False).get_json())
        # for device_id in device_3_ids.intersection(device_5_ids):
                # with client:
                #     results_3_5.append(
                #         client.get(
                #         f"/api/device/{device_id}",
                #         follow_redirects=False).get_json())
        # for device_id in device_2_ids:
           #      with client:
           #          results_some_2.append(
           #              client.get(
           #              f"/api/device/{device_id}",
           #              follow_redirects=False).get_json())

        # assert all( result['role'] == expected_only_3_role for result in results_only_3 )
        # assert all( result['role'] == expected_only_5_role for result in results_only_5 )
        # assert all( result['role'] == expected_3_5_role for result in results_3_5 )
        # assert any( result['role'] == expected_some_2_role for result in results_some_2 )