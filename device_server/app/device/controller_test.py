from flask.testing import FlaskClient

from app.test.fixtures import client, app
from app.test.devices import device_3_ids, device_5_ids, device_2_ids

def test_get(client: FlaskClient):
    expected_only_3_role = 'Bing'
    expected_only_5_role = 'Bang'
    expected_3_5_role = 'Boom'
    expected_some_2_role = 'Meh'

    results_only_3, results_only_5, results_3_5, results_some_2 = ([] for _ in range(4))

    for device_id in device_3_ids.difference(device_5_ids):
	        with client:
	            results_only_3.append(
	            	client.get(
	                f"/api/device/{device_id}",
	                follow_redirects=False).get_json())
    for device_id in device_5_ids.difference(device_3_ids):
	        with client:
	            results_only_5.append(
	            	client.get(
	                f"/api/device/{device_id}",
	                follow_redirects=False).get_json())
    for device_id in device_3_ids.intersection(device_5_ids):
	        with client:
	            results_3_5.append(
	            	client.get(
	                f"/api/device/{device_id}",
	                follow_redirects=False).get_json())
    for device_id in device_2_ids:
	        with client:
	            results_some_2.append(
	            	client.get(
	                f"/api/device/{device_id}",
	                follow_redirects=False).get_json())

    assert all( result['role'] == expected_only_3_role for result in results_only_3 )
    assert all( result['role'] == expected_only_5_role for result in results_only_5 )
    assert all( result['role'] == expected_3_5_role for result in results_3_5 )
    assert any( result['role'] == expected_some_2_role for result in results_some_2 )