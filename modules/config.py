__author__ = 'ripster'

import yaml


def load_config(file_name):
    with open(file_name, 'r') as f:
        conf = yaml.load(f.read())

    return Config(conf)

class Config:
    def __init__(self, cfg):
        self.__validate_config(cfg)

    @staticmethod
    def __validate_config(conf):
        # Proper config structure
        sections = {'irc':
                        {'connection': {'network': str,
                                        'port': int,
                                        'ssl': bool},
                         'channels': list,
                         'user': {'nickname': str,
                                  'realname': str,
                                  'password': str,
                                  'operpass': str},
                         'auth': {'oper': bool,
                                  'nicksrv': bool, 'opersrv': bool}
                         }
                    }
        # Validate config
        for section in sections:
            if section not in conf:
                raise ConfigError("Section '%s' is missing in config." % section)

            for subsection in sections[section]:
                if subsection not in conf[section]:
                    raise ConfigError("Section '%s' is missing in config." % subsection)

                if isinstance(sections[section][subsection], dict):
                    for parameter in sections[section][subsection]:
                        if parameter not in conf[section][subsection]:
                            raise ConfigError("Parameter '%s' is missing in config." % parameter)
                elif not isinstance(conf[section][subsection], sections[section][subsection]):
                    raise TypeError('%s is not the correct type.' % subsection)

    def print_config(self):
        print(self.conf)
      
        
class ConfigError(Exception):
    def __init__(self, message):
        super(ConfigError, self).__init__(message)
