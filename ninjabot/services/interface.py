__author__ = 'ripster'

import services
import greeter


Greeter = greeter.Greeter()

def reload_services():
    reload(services)
    reload(greeter)

class Services:
    def __init__(self, irc):
        self.irc = irc

    def userJoined(self, user, channel):
        for service in services.service_list:
            self.__send_message(service.userJoined(user, channel))

    def __send_message(self, message):
        if isinstance(message, str):
            self.irc.sendLine(message)
        elif isinstance(message, list):
            for msg in message:
                self.irc.sendLine(msg)
