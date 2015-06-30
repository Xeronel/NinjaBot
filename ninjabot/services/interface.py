__author__ = 'Harmless'


__userjoined = []
service = []
def register_userJoined(service):
    __userjoined.append(service)
def notify_userJoined():
    for service in __userjoined:
        service.userjoined()

def userjoined():
    pass

def userkicked():
    pass

def userqueued():
    pass

def useryourmom():
    pass