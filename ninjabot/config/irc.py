__author__ = 'ripster'

from collections import namedtuple
from config import ConfigError, BaseConfig


class Config(BaseConfig):
    def __init__(self):
        skeleton = {'network': {'address': str,
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
        BaseConfig.__init__(self, 'config.yaml', skeleton)

    @property
    def network(self):
        c = namedtuple('network', ['address', 'port', 'ssl'])
        c.address = self.cfg_dict['network']['address']
        c.port = self.cfg_dict['network']['port']
        c.ssl = self.cfg_dict['network']['ssl']
        return c

    @property
    def channels(self):
        return self.cfg_dict['channels']

    @property
    def user(self):
        user = namedtuple('user', ['nickname',
                                   'realname',
                                   'operpass',
                                   'password'])
        user.nickname = self.cfg_dict['user']['nickname']
        user.realname = self.cfg_dict['user']['realname']
        user.operpass = self.cfg_dict['user']['operpass']
        user.password = self.cfg_dict['user']['password']
        return user

    @property
    def auth(self):
        auth = namedtuple('auth', ['oper', 'nicksrv', 'opersrv'])
        auth.oper = self.cfg_dict['auth']['oper']
        auth.nicksrv = self.cfg_dict['auth']['nicksrv']
        auth.opersrv = self.cfg_dict['auth']['opersrv']
        return auth
