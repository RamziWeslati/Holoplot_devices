from .model import Device

class DeviceService:
    @staticmethod
    def get_role(device_id: int) -> int:
        """Maps a device to it's role
        params:
        - device_id: int

        returns:
        role: str: fetched from config
        """
        _device = Device(device_id)
        return _device.role
