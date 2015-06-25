__author__ = 'ripster'

import yaml

class ConfigError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class BaseConfig:
    def __init__(self, file_name, skeleton, validation_method):
        self.file_name = file_name
        self.cfg_dict = self.__load()
        validation_method(self.cfg_dict, skeleton)

    def __load(self):
        with open(self.file_name, 'r') as f:
            conf = yaml.load(f.read())

        return conf
