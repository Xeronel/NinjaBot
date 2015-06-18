__author__ = 'ripster'

from twisted.internet import reactor, protocol
from twisted.words.protocols import irc
import twisted.internet as inet


class IRCClient(irc.IRCClient):
    def __init__(self, nickname):
        self.nickname = nickname

    def signedOn(self):
        self.join(self.factory.channel)
        self.sendLine('/oper ripster test')


class IRCFactory(protocol.ClientFactory):
    def __init__(self, channel, nickname):
        self.channel = channel
        self.nickname = nickname

    def buildProtocol(self, addr):
        proto = IRCClient(self.nickname)
        proto.factory = self
        return proto

    def clientConnectionLost(self, connector, reason):
        # Try to reconnect if disconnected.
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()


reactor.connectTCP('irc.ratio.ninja', 6697, IRCFactory('#rationinja', 'RipBot'))
reactor.run()
print('reactor running')