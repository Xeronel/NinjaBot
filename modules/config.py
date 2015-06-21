__author__ = 'ripster'

import yaml
from collections import namedtuple


def load_config(file_name):
    with open(file_name, 'r') as f:
        conf = yaml.load(f.read())

    return Config(conf)

class Config:
    def __init__(self, cfg):
        self.__validate_config(cfg)
        self.__irc_cfg = IrcConfig(cfg['irc'])

    @property
    def irc(self):
            return self.__irc_cfg

    @staticmethod
    def __validate_config(conf):
        # Proper config structure
        sections = {'irc':
                        {'network': {'address': str,
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


class IrcConfig:
    def __init__(self, cfg):
        self.__cfg = cfg

    @property
    def network(self):
        c = namedtuple('network', ['address', 'port', 'ssl'])
        c.address = self.__cfg['network']['address']
        c.port = self.__cfg['network']['port']
        c.ssl = self.__cfg['network']['ssl']
        return c

    @property
    def channels(self):
        return self.__cfg['channels']

    @property
    def user(self):
        user = namedtuple('user', ['nickname',
                                   'realname',
                                   'operpass',
                                   'password'])
        user.nickname = self.__cfg['user']['nickname']
        user.realname = self.__cfg['user']['realname']
        user.operpass = self.__cfg['user']['operpass']
        user.password = self.__cfg['user']['password']
        return user

    @property
    def auth(self):
        auth = namedtuple('auth', ['oper', 'nicksrv', 'opersrv'])
        auth.oper = self.__cfg['auth']['oper']
        auth.nicksrv = self.cfg['auth']['nicksrv']
        auth.opersrv = self.cfg['auth']['opersrv']
        return auth


class ConfigError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)
