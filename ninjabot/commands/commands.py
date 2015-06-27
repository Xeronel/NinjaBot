__author__ = 'ripster'

class BaseCommand(object):
    def __init__(self):
        # Word that causes the command to run
        self.trigger = ''
        # Command description
        self.help = ''
        # Example of how to use the command
        self.usage = ''
        # Groups allowed to run the command
        self.allow = []

    def execute(self, user, channel):
        pass
