__author__ = 'ripster'

import yaml

class ConfigError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class BaseConfig:
    def __init__(self, file_name, skeleton):
        self.file_name = file_name
        self.cfg_dict = self.__load()
        validate_config(self.cfg_dict, skeleton)

    def __load(self):
        with open(self.file_name, 'r') as f:
            conf = yaml.load(f.read())

        return conf

def validate_config(sections, cfg):
    for section in sections:
        # Make sure the section is in the config
        if section not in cfg:
            raise ConfigError("Section '%s' is missing in config." % section)

        if isinstance(sections[section], dict):
            for parameter in sections[section]:
                # Make sure the parameters are all there
                if parameter not in cfg[section]:
                    raise ConfigError("Parameter '%s' is missing in config." % parameter)

                # Make sure the parameters are the correct data type
                if not isinstance(cfg[section][parameter], sections[section][parameter]):
                    raise TypeError('%s contains invalid data.' % parameter)

        elif not isinstance(cfg[section], sections[section]):
            raise TypeError('%s contains invalid data.' % section)
