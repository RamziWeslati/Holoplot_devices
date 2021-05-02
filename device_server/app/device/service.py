from .model import Device

class DeviceService:
    @staticmethod
    def get_role(device_id: int) -> int:
        _device = Device(device_id)
        return _device.role
