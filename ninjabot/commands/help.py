__author__ = 'ripster'

from ninjabot.types import BaseCommand


class Help(BaseCommand):
    def __init__(self, irc):
        BaseCommand.__init__(self, irc)

        # Word that causes the command to run
        self.trigger = 'help'
        # Command description
        self.help = 'Join the #help channel'
        # Example of how to use the command
        self.usage = 'help <user>'
        # Groups allowed to run the command
        self.allow = ['*']

    def execute(self, user, mode, channel, args):
        if mode == '~' and len(args) == 2:
            result = self.move(args[1])
        else:
            result = self.move(user)

        return result

    @staticmethod
    def move(user):
        return 'sajoin %s %s' % (user, '#help')
