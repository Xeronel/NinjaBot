__author__ = 'ripster'

class BaseCommand(object):
    def __init__(self):
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
