__author__ = 'ripster'

from types import BaseEvents
from ninjabot import services, commands


class EventHandler(BaseEvents):
    def __init__(self, irc):
        BaseEvents.__init__(self, irc)
        self.commands = {}

        # Load commands into a dictionary
        for cls in commands.__dict__.items():
            if isinstance(cls[1], type):
                cmd = cls[1](irc)
                self.commands[cmd.trigger] = cmd

        # Load services into a list
        self.services = [service[1](irc) for service in services.__dict__.items() if isinstance(service[1], type)]

    def userJoined(self, user, channel):
        for service in self.services:
            self.__send_message(service.userJoined(user, channel))

        for command in self.commands:
            self.__send_message(self.commands[command].userJoined(user, channel))

    def userLeft(self, user, channel):
        for service in self.services:
            self.__send_message(service.userLeft(user, channel))

        for command in self.commands:
            self.__send_message(self.commands[command].userLeft(user, channel))

    def privmsg(self, user, channel, message):
        # Get the first word without the first character
        trigger = message.partition(' ')[0][1:]

        for service in self.services:
            self.__send_message(service.privmsg(user, channel, message))

        for command in self.commands:
            if trigger == command:
                self.__send_message(self.commands[command].privmsg(user, channel, message))

    def __send_message(self, message):
        if isinstance(message, str):
            self.irc.sendLine(message)
        elif isinstance(message, list):
            for msg in message:
                self.irc.sendLine(msg)
