__author__ = 'ripster'

import kick
import help


Kick = kick.Kick()
Help = help.Help()

commands = {Kick.trigger: Kick,
            Help.trigger: Help}

def reload_cmds():
    reload(kick)
    reload(help)

def run_command(irc, user, mode, channel, message):
    msg = message.split(' ')
    cmd = msg[0][1:]
    is_cmd = True if cmd in commands else False

    if is_cmd:
        try:
            result = commands[cmd].execute(irc, user, mode, channel, msg)
        except Exception as e:
            result = 'PRIVMSG %s :Error running %s command (%s)' % (channel, cmd, e.message)
    else:
        result = None

    return result
