__author__ = 'ripster'

from config import BaseConfig, ConfigError
from collections import namedtuple


class Config(BaseConfig):
    def __init__(self):
        BaseConfig.__init__(self, 'groups.yaml', validate_config)

    def groups(self):
        return self.cfg_dict.keys()


def validate_config():
    pass
