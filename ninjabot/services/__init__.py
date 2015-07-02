__author__ = 'ripster'
__all__ = ['Services', 'reload_services']

from interface import Services


def reload_services():
    interface.reload_services()
    reload(interface)
