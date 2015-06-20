__author__ = 'ripster'

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor, ssl


class IRCClient(irc.IRCClient):
    def __init__(self, nickname, channels):
        self.nickname = nickname
        self.channels = channels

    def signedOn(self):
        for channel in self.channels:
            self.join(channel)


class IRCFactory(protocol.ClientFactory):
    def __init__(self, channels, nickname):
        self.channels = channels
        self.nickname = nickname

    def buildProtocol(self, address):
        proto = IRCClient(self.nickname, self.channels)
        proto.factory = self
        return proto

    def clientConnectionLost(self, connector, reason):
        # Try to reconnect if disconnected.
        print(reason.getErrorMessage())
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print(reason.getErrorMessage())
        reactor.stop()


def run(cfg):
    if cfg.irc.network.ssl:
        reactor.connectSSL(cfg.irc.network.address,
                           cfg.irc.network.port,
                           IRCFactory(cfg.irc.channels,
                                      cfg.irc.user.nickname),
                           ssl.ClientContextFactory())
    else:
        reactor.connectTCP(cfg.irc.network.address,
                           cfg.irc.network.port,
                           IRCFactory(cfg.irc.channels,
                                      cfg.irc.user.nickname))
    reactor.run()
