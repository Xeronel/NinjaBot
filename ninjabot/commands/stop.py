__author__ = 'ripster'

from ninjabot.basetypes import BaseCommand


class Stop(BaseCommand):
    def __init__(self, irc):
        # Initialize Base
        BaseCommand.__init__(self, irc)
        # Word that causes the command to run
        self.trigger = 'stop'
        # Command description
        self.help = 'Stop the ninjabot'
        # Example of how to use the command
        self.usage = '!stop'
        # Groups allowed to run the command
        self.allow = ['~', '&']

    def execute(self, user, mode, channel, args):
        if self.is_allowed(mode):
            self.irc.quit()
        else:
            return self.message(channel, 'You are not allowed to run that command.')
