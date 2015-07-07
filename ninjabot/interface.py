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


def run_command(user, mode, channel, message):
    """
    :param irc: IRC Client
    :param user: Executor of the command
    :param mode: Mode of the user (~, &, @, %, *)
    :param channel: Channel the command was run in
    :param message: The users message
    :return: True if command was run, else False
    """
    msg = message.split(' ')
    cmd = msg[0][1:].lower()
    is_cmd = True if cmd in commands else False

    if is_cmd:
        try:
            result = commands[cmd].execute(user, mode, channel, msg)
        except Exception as e:
            result = 'PRIVMSG %s :Error running %s command (%s)' % (channel, cmd, e.message)
    else:
        result = None

    try:
        if isinstance(result, list) or isinstance(result, tuple):
            for i in result:
                irc.sendLine(i)
            return True
        elif isinstance(result, str):
            irc.sendLine(result)
            return True
        else:
            return False
    except Exception as e:
        irc.sendLine('PRIVMSG %s :Error running %s command (%s)' % (channel, message, e.message))
        return False
