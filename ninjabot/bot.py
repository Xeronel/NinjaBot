__author__ = 'ripster'

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor, ssl
import commands as cmd
import config


class IRCClient(irc.IRCClient):
    def __init__(self, nickname, channels, modes):
        self.nickname = nickname
        self.channels = channels
        self.supp_modes = modes  # Modes supported by the IRC server
        self.users = {}  # User dict organized by channel and mode

    def signedOn(self):
        for channel in self.channels:
            self.join(channel)

    def joined(self, channel):
        self.getUserModes('#' + channel)

    def privmsg(self, user, channel, message):
        if message.startswith('!reload'):
            cmd.reload_cmds()
            reload(cmd)

        if message.startswith('!'):
            self.sendLine(cmd.run_command(user, channel, message))

        if user.startswith('Ripster!') and message == '!stop':
            print('%s issued stop command.' % user.split('!')[0])
            self.quit()

    def modeChanged(self, user, channel, set, modes, args):
        print('Mode set %s %s applied to %s in channel %s' % (set, modes, user, channel))

    def irc_RPL_NAMREPLY(self, prefix, params):
        channel = params[2]
        user_list = params[3].strip().split(' ')

        if channel not in self.users:
            self.users[channel] = {}

        if '*' not in self.users[channel]:
            self.users[channel]['*'] = []

        for user in user_list:
            mode = user[0]

            if mode in self.supp_modes:
                if mode not in self.users:
                    self.users[channel][mode] = []
                self.users[channel][mode].append(user[1:])
            else:
                self.users[channel]['*'].append(user)

        print(self.users)

    def getUserModes(self, channel):
        self.sendLine('names #%s' % channel)


class IRCFactory(protocol.ClientFactory):
    def __init__(self, nickname, channels, modes):
        self.nickname = nickname
        self.channels = channels
        self.modes = modes

    def buildProtocol(self, address):
        proto = IRCClient(self.nickname, self.channels, self.modes)
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
                           IRCFactory(irc_cfg.user.nickname,
                                      irc_cfg.channels,
                                      irc_cfg.modes),
                           ssl.ClientContextFactory())
    else:
        reactor.connectTCP(irc_cfg.irc.network.address,
                           irc_cfg.irc.network.port,
                           IRCFactory(irc_cfg.user.nickname,
                                      irc_cfg.channels,
                                      irc_cfg.modes))
    reactor.run()
