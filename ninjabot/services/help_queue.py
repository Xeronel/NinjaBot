__author__ = 'ripster'

from ninjabot.types import BaseEvent


class HelpQueue(BaseEvent):
    def __init__(self, irc):
        BaseEvent.__init__(self, irc)
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