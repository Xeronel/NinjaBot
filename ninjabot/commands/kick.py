__author__ = 'ripster'

from ninjabot.basetypes import BaseCommand


class Kick(BaseCommand):
    def __init__(self, irc):
        BaseCommand.__init__(self, irc)

        # Word that causes the command to run
        self.trigger = 'kick'
        # Command description
        self.help = 'Kick the user from the channel'
        # Example of how to use the command
        self.usage = 'kick <user> <reason>'
        # Groups allowed to run the command
        self.allow = ['~', '&', '@']
        # Protected groups
        self.protected = ['~', '&']

    def execute(self, user, mode, channel, message):
        try:
            target = message[1]
        except IndexError:
            target = ''

        if target == self.irc.nickname:
            return self.message(channel, 'Fuck off!')

        if self.is_allowed(mode):
            if mode not in self.protected and \
            self.irc.users[target][channel] in self.protected:
                return self.kick(channel, user, 'Nice try')
            else:
                if len(message) == 2:
                    return self.kick(channel, target)
                elif len(message) > 2:
                    return self.kick(channel, target, ' '.join(message[2:]))
                else:
                    return self.message(channel, 'Usage is "%s"' % self.usage)
        else:
            return self.denied(channel)

    @staticmethod
    def kick(channel, user, reason=''):
        if reason != '':
            return 'KICK %s %s %s' % (channel, user, reason)
        else:
            return 'KICK %s %s' % (channel, user)
