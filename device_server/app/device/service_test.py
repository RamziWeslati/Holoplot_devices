from app.test.fixtures import app
from app.test.devices import device_3_ids, device_5_ids, device_2_ids
from .service import DeviceService

def test_device_roles():
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
