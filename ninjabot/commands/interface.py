__author__ = 'ripster'

from kick import Kick
from help import Help

help = Help()
kick = Kick()

commands = {kick.trigger: kick,
            help.trigger: help}


def run_command(user, channel, message):
    msg = message.split(' ')
    cmd = msg[0][1:]
    is_cmd = True if cmd in commands else False

    if is_cmd:
        try:
            result = commands[cmd].execute(user, channel, message)
        except Exception as e:
            result = 'PRIVMSG %s :Error running %s command (%s)' % (channel, cmd, e.message)
    else:
        result = 'That is not a command!'

    return result
