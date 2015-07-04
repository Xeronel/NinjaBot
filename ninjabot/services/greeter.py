__author__ = 'ripster'

from ninjabot.events import Event


class Greeter(Event):
    def __init__(self, irc):
        Event.__init__(self, irc)

    def userJoined(self, user, channel):
        if channel == '#help':
            return [self.message(channel, 'Welcome to Ratio Ninja live support.'),
                    self.message(channel, 'Please wait and someone will help you shortly.')]
