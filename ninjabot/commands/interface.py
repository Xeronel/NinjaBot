__author__ = 'ripster'

import kick
import help
import stop


# Instantiate command classes
Kick = kick.Kick()
Help = help.Help()
Stop = stop.Stop()

# List of commands
commands = {Kick.trigger: Kick,
            Help.trigger: Help,
            Stop.trigger: Stop}

def reload_cmds():
    reload(kick)
    reload(help)
    reload(stop)


def run_command(irc, user, mode, channel, message):
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
            result = commands[cmd].execute(irc, user, mode, channel, msg)
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
