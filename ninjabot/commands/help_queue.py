__author__ = 'ripster'

from ninjabot.types import BaseCommand


class HelpQueue(BaseCommand):
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
        self.excluded_modes = ['~', '&', '@', '%']
        self.user_queue = []

    def userJoined(self, user, channel):
        mode, user = self.irc.parse_user(user)

        if mode not in self.excluded_modes:
            if user not in self.user_queue:
                self.user_queue.append(user)

    def userLeft(self, user, channel):
        if user in self.user_queue:
            del(self.user_queue[user])

    def privmsg(self, user, channel, message):
        print(message)

    def nextUser(self, user, channel):
        self.user_queue.pop()

    def showQueue(self):
        return len(self.user_queue)
