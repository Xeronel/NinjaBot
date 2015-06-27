__author__ = 'ripster'

from kick import Kick
from help import Help

help = Help()
kick = Kick()

commands = [kick, help]
triggers = [kick.trigger, help.trigger]


def run_command(msg):
    msg = msg.partition(' ')[0]
    cmd = msg[0]
    args = msg[1:]
    print(cmd, args)

