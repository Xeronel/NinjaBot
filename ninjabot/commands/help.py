__author__ = 'ripster'

from command import Command


class Help(Command):
    def __init__(self):
        Command.__init__(self)

        # Word that causes the command to run
        self.trigger = 'help'
        # Command description
        self.help = 'Join the #help channel'
        # Example of how to use the command
        self.usage = 'help <user>'
        # Groups allowed to run the command
        self.allow = ['all']

    def execute(self):
        pass
