__author__ = 'ripster'
__all__ = ['Services']

from interface import Services


def reload_cmds():
    interface.reload_services()
    reload(interface)
