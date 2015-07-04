__author__ = 'ripster'
__all__ = ['Services', 'reload_services', 'run_command', 'reload_cmds']

from interface import run_command, Services


def reload_cmds():
    interface.reload_cmds()
    reload(interface)

def reload_services():
    interface.reload_services()
    reload(interface)
