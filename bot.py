__author__ = 'ripster'

from twisted.internet import reactor, ssl
from modules import irc


reactor.connectSSL('irc.ratio.ninja',
                   6697,
                   irc.IRCFactory('#rationinja', 'RipBot', reactor),
                   ssl.ClientContextFactory())
reactor.run()
