__author__ = 'ripster'

from ninjabot.types import BaseCommand
from ninjabot.services.help_queue import help_queue


class Next(BaseCommand):
    def __init__(self, irc):
        BaseCommand.__init__(self, irc)
        # Word that causes the command to run
        self.trigger = '!next'
        # Groups allowed to run the command
        self.allow = ['~', '&', '@', '%']
        # Command description
        self.help = 'Retrieves the next user in the queue'
        # Example of how to use the command
        self.usage = '!next'
        self.protected = ['~', '&', '@', '%']

    def execute(self, user, mode, channel, args):
        pass

    def userLeft(self, user, channel):
        if user in help_queue:
            del(help_queue[user])

    def privmsg(self, user, channel, message):
        print(message)

    def nextUser(self, user, channel):
        help_queue.pop()

    def showQueue(self):
        return len(help_queue)


class List(BaseCommand):
    def __init__(self, irc):
        BaseCommand.__init__(self, irc)
        # Word that causes the command to run
        self.trigger = '!list'
        # Groups allowed to run the command
        self.allow = ['~', '&', '@', '%']
        # Command description
        self.help = 'Retrieves the list of users in the queue'
        # Example of how to use the command
        self.usage = '!list'

    def execute(self, user, mode, channel, args):
        pass


class Clear(BaseCommand):
    def __init__(self, irc):
        BaseCommand.__init__(self, irc)
        # Word that causes the command to run
        self.trigger = '!clear'
        # Groups allowed to run the command
        self.allow = ['~', '&', '@', '%']
        # Command description
        self.help = 'Clears the list of users in the queue'
        # Example of how to use the command
        self.usage = '!clear'

    def execute(self, user, mode, channel, args):
        pass
