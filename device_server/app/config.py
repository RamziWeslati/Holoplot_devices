import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """common config
    - ROLES_BY_MULTIPLIER: dict: 
        configuration for device role mapping,
        key: int: multiplier to map ids
        value: str: device role
    - ROLE_ALL_MULTIPLIERS: str: role of devices that map to all multiplier roles
    - ROLE_NONE_MULTIPLIERS: str: role of devices that do not map to any multiplier roles
    """
    CONFIG_NAME = "base"
    DEBUG = False
    ROLES_BY_MULTIPLIER = {
        3: 'Bing',
        5: 'Bang',
    }
    ROLE_ALL_MULTIPLIERS = 'Boom'
    ROLE_NONE_MULTIPLIERS = 'Meh'


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False
    TESTING = False


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}