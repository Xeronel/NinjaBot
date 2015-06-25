__author__ = 'ripster'

from command import Command


class Kick(Command):
    def __init__(self):
        Command.__init__(self)

        # Word that causes the command to run
        self.trigger = 'kick'
        # Command description
        self.help = 'Kick the user from the channel'
        # Example of how to use the command
        self.usage = 'kick <user> <reason>'
        # Groups allowed to run the command
        self.allow = ['admin']

    def execute(self):
        pass
