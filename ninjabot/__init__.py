__author__ = 'ripster'
__all__ = ['EventHandler']

import interface
from interface import EventHandler


def reload_package():
    interface.reload_all()
    reload(interface)
