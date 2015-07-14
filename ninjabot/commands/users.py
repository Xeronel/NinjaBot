__author__ = 'ripster'

from ninjabot.basetypes import BaseCommand


class Users(BaseCommand):
    def __init__(self, irc):
        # Initialize Base
        BaseCommand.__init__(self, irc)
        # Word that causes the command to run
        self.trigger = 'users'
        # Command description
        self.help = 'List the users currently stored by the bot'
        # Example of how to use the command
        self.usage = '!users'
        # Groups allowed to run the command
        self.allow = ['~', '&']

    def execute(self, user, mode, channel, args):
        if self.is_allowed(mode):
            for user in self.irc.users:
                self.irc.sendLine(self.message(channel, user))
        else:
            return self.denied(channel)
