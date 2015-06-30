__author__ = 'Harmless'

class BaseServices(object):
    def __init__(self):
        # Service description
        self.help = ''
        # Example of how the service performs
        self.usage = ''
        # Groups allowed to run the service
        self.allow = []

    @staticmethod
    def message(channel, message):
        return 'PRIVMSG %s :%s' % (channel, message)

    def userjoined(self):
        pass

    def noticed(self):
        pass
