__author__ = 'ripster'

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor, ssl
import config


class IRCClient(irc.IRCClient):
    def __init__(self, nickname, channels):
        self.nickname = nickname
        self.channels = channels

    def signedOn(self):
        for channel in self.channels:
            self.join(channel)

    def privmsg(self, user, channel, message):
        if user.startswith('Ripster!') and message == '!stop':
            print('%s issued stop command.' % user.split('!')[0])
            self.quit()


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


def run():
    irc_cfg = config.Irc()
    if irc_cfg.network.ssl:
        reactor.connectSSL(irc_cfg.network.address,
                           irc_cfg.network.port,
                           IRCFactory(irc_cfg.channels,
                                      irc_cfg.user.nickname),
                           ssl.ClientContextFactory())
    else:
        reactor.connectTCP(irc_cfg.irc.network.address,
                           irc_cfg.irc.network.port,
                           IRCFactory(irc_cfg.channels,
                                      irc_cfg.user.nickname))
    reactor.run()
