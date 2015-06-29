__author__ = 'ripster'

from commands import BaseCommand


class Kick(BaseCommand):
    def __init__(self):
        BaseCommand.__init__(self)

        # Word that causes the command to run
        self.trigger = 'kick'
        # Command description
        self.help = 'Kick the user from the channel'
        # Example of how to use the command
        self.usage = 'kick <user> <reason>'
        # Groups allowed to run the command
        self.allow = ['~', '&', '@']

    def execute(self, irc, user, mode, channel, args):
        protected = ['~', '&']
        try:
            target = args[1]
        except IndexError:
            target = ''

        if target == irc.nickname:
            return self.message(channel, 'Fuck off!')

        if self.is_allowed(mode):
            if mode not in protected and irc.users[target][channel] in protected:
                return self.kick(channel, user, 'Nice try')
            else:
                if len(args) == 2:
                    return self.kick(channel, target)
                elif len(args) > 2:
                    return self.kick(channel, target, ' '.join(args[2:]))
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
