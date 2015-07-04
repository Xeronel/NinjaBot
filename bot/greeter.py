__author__ = 'ripster'

from services import Events


class Greeter(Events):
    def __init__(self, irc):
        Events.__init__(self, irc)

    def userJoined(self, user, channel):
        if channel == '#help':
            return [self.message(channel, 'Welcome to Ratio Ninja live support.'),
                    self.message(channel, 'Please wait and someone will help you shortly.')]
