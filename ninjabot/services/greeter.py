__author__ = 'ripster'

from ninjabot.types import BaseService


class Greeter(BaseService):
    def __init__(self, irc):
        BaseService.__init__(self, irc)

    def userJoined(self, user, channel):
        if channel == '#help':
            return [self.message(channel, 'Welcome to Ratio Ninja live support.'),
                    self.message(channel, 'Please wait and someone will help you shortly.')]
