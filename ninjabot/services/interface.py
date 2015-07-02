__author__ = 'ripster'

from services import service_list
from greeter import Greeter


greeter = Greeter()

class Services:
    def __init__(self, irc):
        self.irc = irc

    def userJoined(self, user, channel):
        for service in service_list:
            self.__send_message(service.userJoined(user, channel))

    def __send_message(self, message):
        if isinstance(message, str):
            self.irc.sendLine(message)
        elif isinstance(message, list):
            for msg in message:
                self.irc.sendLine(msg)
