__author__ = 'ripster'

from services import BaseServices


class Greeter(BaseServices):
    def __init__(self):
        BaseServices.__init__(self)

    def userJoined(self, user, channel):
        if channel == '#help':
            return self.message(channel, 'Welcome %s' % user)
