__author__ = 'ripster'
__all__ = ['EventHandler', 'reload_services', 'run_command', 'reload_cmds']
__commands__ = ['help', 'kick', 'stop']
__services__ = ['greeter', 'help_queue']

from interface import run_command, EventHandler


def reload_cmds():
    interface.reload_cmds()
    reload(interface)

def reload_services():
    interface.reload_services()
    reload(interface)
