__author__ = 'ripster'


services = []
commands = {}

class BaseEvents(object):
    def __init__(self, irc):
        # IRC Client
        self.irc = irc
        services.append(self)

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


class BaseCommand(BaseEvents):
    def __init__(self, irc):
        BaseEvents.__init__(self, irc)

        # Word that causes the command to run
        self.trigger = ''
        # Command description
        self.help = ''
        # Example of how to use the command
        self.usage = ''
        # Groups allowed to run the command
        self.allow = []

    def execute(self, irc, user, mode, channel, args):
        pass

    def is_allowed(self, mode):
        if '*' in self.allow:
            return True
        elif mode in self.allow:
            return True
        else:
            return False

    @staticmethod
    def message(channel, message):
        return 'PRIVMSG %s :%s' % (channel, message)

    @staticmethod
    def denied(channel):
        return 'PRIVMSG %s :%s' % (channel, 'You are not allowed to run that command.')