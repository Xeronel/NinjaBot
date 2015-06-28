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

def run_command(user, channel, message):
    msg = message.split(' ')
    cmd = msg[0][1:]
    is_cmd = True if cmd in commands else False

    if is_cmd:
        try:
            result = commands[cmd].execute(user, channel, cmd)
        except Exception as e:
            result = 'PRIVMSG %s :Error running %s command (%s)' % (channel, cmd, e.message)
    else:
        result = 'That is not a command!'

    return result
