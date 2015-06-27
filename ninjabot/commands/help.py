__author__ = 'ripster'

from commands import BaseCommand


class Help(BaseCommand):
    def __init__(self):
        BaseCommand.__init__(self)

        # Word that causes the command to run
        self.trigger = 'help'
        # Command description
        self.help = 'Join the #help channel'
        # Example of how to use the command
        self.usage = 'help <user>'
        # Groups allowed to run the command
        self.allow = ['*']

    def execute(self, user, channel, args):
        return 'PRIVMSG %s :%s' % (channel, 'Fuck off!')
