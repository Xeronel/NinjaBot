__author__ = 'ripster'


class BaseEvents(object):
    def __init__(self, irc):
        self.irc = irc

    def userJoined(self, user, channel):
        pass

    def userLeft(self, user, channel):
        pass

    def privmsg(self, user, channel, message):
        pass

    def noticed(self, user, channel, message):
        pass


class BaseEvent(BaseEvents):
    def __init__(self, irc):
        BaseEvents.__init__(self, irc)

        # Modes protected from the command/service
        self.protected = []
        # Command/Service description
        self.help = ''

    @staticmethod
    def message(channel, message):
        return 'PRIVMSG %s :%s' % (channel, message)


class BaseCommand(BaseEvent):
    def __init__(self, irc):
        BaseEvent.__init__(self, irc)

        # Word that causes the command to run
        self.trigger = ''
        # Example of how to use the command
        self.usage = ''
        # Groups allowed to run the command
        self.allow = []

    def execute(self, user, mode, channel, message):
        pass

    def privmsg(self, user, channel, message):
        message = message.split(' ')
        user, mode = self.irc.parse_user(user, channel)
        return self.execute(user, mode, channel, message)

    def is_allowed(self, mode):
        if '*' in self.allow:
            return True
        elif mode in self.allow:
            return True
        else:
            return False

    @staticmethod
    def denied(channel):
        return 'PRIVMSG %s :%s' % (channel, 'You are not allowed to run that command.')
