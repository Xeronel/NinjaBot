__author__ = 'ripster'


service_list = []

class BaseServices(object):
    def __init__(self):
        service_list.append(self)

    def userJoined(self, user, channel):
        pass

    def userLeft(self, user, channel):
        pass

    def privmsg(self, user, channel, message):
        pass

    def noticed(self, user, channel, message):
        pass

    def modeChanged(self, user, channel, set, modes, args):
        pass

    @staticmethod
    def message(channel, message):
        return 'PRIVMSG %s :%s' % (channel, message)
