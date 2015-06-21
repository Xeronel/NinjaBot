__author__ = 'ripster'


class ConfigError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)