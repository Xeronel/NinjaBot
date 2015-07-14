__author__ = 'ripster'

from ninjabot.basetypes import BaseCommand, BaseService

help_queue = []


class HelpQueue(BaseService):
    def __init__(self, irc):
        BaseService.__init__(self, irc)
        # Service description
        self.help = 'Adds a user to the help queue when they join #help'
        # Modes protected from the service
        self.protected = ['~', '&', '@', '%']

    def userJoined(self, user, channel):
        user, mode = self.irc.parse_user(user, channel)

        if mode not in self.protected:
            if user not in help_queue:
                help_queue.append(user)
                print('Added %s to queue' % user)
                print(help_queue)

    def userLeft(self, user, channel):
        user, mode = self.irc.parse_user(user, channel)

        if mode not in self.protected:
            if user in help_queue:
                help_queue.remove(user)
                print('Removed %s from queue' % user)
