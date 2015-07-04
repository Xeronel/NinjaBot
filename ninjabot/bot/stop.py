__author__ = 'ripster'

from commands import BaseCommand

class Stop(BaseCommand):
    def __init__(self):
        # Initialize Base
        BaseCommand.__init__(self)
        # Word that causes the command to run
        self.trigger = 'stop'
        # Command description
        self.help = 'Stop the bot'
        # Example of how to use the command
        self.usage = '!stop'
        # Groups allowed to run the command
        self.allow = ['~', '&']

    def execute(self, irc, user, mode, channel, args):
        if self.is_allowed(mode):
            irc.quit()
        else:
            return self.message(channel, 'You are not allowed to run that command.')
