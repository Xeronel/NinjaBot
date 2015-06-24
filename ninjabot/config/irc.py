__author__ = 'ripster'

import yaml
from collections import namedtuple
from errors import ConfigError


def load(file_name):
    with open(file_name, 'r') as f:
        conf = yaml.load(f.read())

    return Config(conf)


class Config:
    def __init__(self, cfg):
        self.sections = {'network': {'address': str,
                                     'port': int,
                                     'ssl': bool},
                         'channels': list,
                         'user': {'nickname': str,
                                  'realname': str,
                                  'password': str,
                                  'operpass': str},
                         'auth': {'oper': bool,
                                  'nicksrv': bool,
                                  'opersrv': bool}
                         }
        self.__validate_config(cfg)
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
        auth.nicksrv = self.__cfg['auth']['nicksrv']
        auth.opersrv = self.__cfg['auth']['opersrv']
        return auth

    def __validate_config(self, cfg):
        for section in self.sections:
            # Make sure the section is in the config
            if section not in cfg:
                raise ConfigError("Section '%s' is missing in config." % section)

            if isinstance(self.sections[section], dict):
                for parameter in self.sections[section]:
                    # Make sure the parameters are all there
                    if parameter not in cfg[section]:
                        raise ConfigError("Parameter '%s' is missing in config." % parameter)

                    # Make sure the parameters are the correct data type
                    if not isinstance(cfg[section][parameter], self.sections[section][parameter]):
                        raise TypeError('%s contains invalid data.' % parameter)

            elif not isinstance(cfg[section], self.sections[section]):
                raise TypeError('%s contains invalid data.' % section)
