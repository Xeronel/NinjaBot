__author__ = 'ripster'
__all__ = ['run_command']

from interface import run_command

def reload_cmds():
    interface.reload_cmds()
    reload(interface)
