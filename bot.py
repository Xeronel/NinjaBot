__author__ = 'ripster'

from twisted.internet import reactor, ssl
from modules import irc, config


conf = config.load_config('config.yaml')
reactor.connectSSL(conf.irc.network.address,
                   conf.irc.network.port,
                   irc.IRCFactory(conf.irc, reactor),
                   ssl.ClientContextFactory())
reactor.run()
