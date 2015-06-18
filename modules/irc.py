__author__ = 'ripster'

from twisted.words.protocols import irc
from twisted.internet import protocol


class IRCClient(irc.IRCClient):
    def __init__(self, nickname):
        self.nickname = nickname

    def signedOn(self):
        for channel in self.factory.channels:
            self.join(channel)


class IRCFactory(protocol.ClientFactory):
    def __init__(self, cfg, reactor):
        self.channels = cfg.channels
        self.nickname = cfg.user.nickname
        self.reactor = reactor

    def buildProtocol(self, addr):
        proto = IRCClient(self.nickname)
        proto.factory = self
        return proto

    def clientConnectionLost(self, connector, reason):
        # Try to reconnect if disconnected.
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        # There is probably a better way to do this
        self.reactor.stop()
