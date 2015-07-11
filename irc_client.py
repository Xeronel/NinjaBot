__author__ = 'ripster'

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor, ssl
import ninjabot
import config
import types


class IRCClient(irc.IRCClient):
    def __init__(self, cfg):
        self.nickname = cfg.user.nickname
        self.operpass = cfg.user.operpass
        if cfg.auth.nicksrv:
            self.password = cfg.user.password
        self.channels = cfg.channels
        self.supp_modes = cfg.modes  # Modes supported by the IRC server
        self.users = {}  # User dict organized by channel and mode
        self.cfg = cfg
        self.bot = ninjabot.EventHandler(self)

    def signedOn(self):
        """
        Auth and join channels
        :return: None
        """
        # Login as oper
        if self.cfg.auth.opersrv and self.operpass != '':
            self.sendLine('oper bot %s' % self.operpass)

        # Auth with OperSrv
        if self.cfg.auth.oper and self.operpass != '':
            # Login with operserv
            self.msg('opersrv', 'login %s' % self.operpass)

        # Join channels
        for channel in self.channels:
            self.join(channel)

    def userJoined(self, user, channel):
        self.bot.userJoined(user, channel)

    def userLeft(self, user, channel):
        if user in self.users and channel in self.users[user]:
            del(self.users[user][channel])

        self.bot.userLeft(user, channel)

    def modeChanged(self, user, channel, set, modes, args):
        if channel[0] == '#':
            print('%s\'s mode changed in %s' % (args[0], channel))
            self.request_modes(channel)

    def privmsg(self, user, channel, message):
        user, mode = self.parse_user(user, channel)
        if message == '!reload' and mode in ('~', '&'):
            ninjabot.reload_package()
            reload(ninjabot)
            self.bot = ninjabot.EventHandler(self)
            self.say(channel, 'Successfully reloaded!')

        self.bot.privmsg(user, channel, message)

    def parse_user(self, user, channel):
        user = user.partition('!')[0]
        if user not in self.users:
            self.request_modes(channel)
        mode = self.users[user][channel]
        return user, mode

    def request_modes(self, channel):
        """
        Send a request for a list of user modes from the specified channel
        :param channel: The channel to request user modes from
        :return: None
        """
        # Triggers irc_RPL_NAMREPLY
        print('Requesting modes for %s' % channel)
        self.sendLine('names %s' % channel)

    def irc_RPL_NAMREPLY(self, prefix, params):
        channel = params[2]
        user_list = params[3].strip().split(' ')

        for user in user_list:
            # Extract the users mode
            mode = user[0]
            if mode in self.supp_modes:
                user = user[1:]
            else:
                mode = '*'

            # Make sure the user is in the dictionary
            if user not in self.users:
                self.users[user] = {}

            # Add the channel to the user
            if channel not in self.users[user]:
                self.users[user][channel] = ''

            if self.users[user][channel] != mode:
                print('Added %s%s in %s' % (mode, user, channel))

            # Set the channel mode
            self.users[user][channel] = mode


class IRCFactory(protocol.ClientFactory):
    def __init__(self, cfg):
        self.cfg = cfg

    def buildProtocol(self, address):
        proto = IRCClient(self.cfg)
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
                           IRCFactory(irc_cfg),
                           ssl.ClientContextFactory())
    else:
        reactor.connectTCP(irc_cfg.network.address,
                           irc_cfg.network.port,
                           IRCFactory(irc_cfg))
    reactor.run()


if __name__ == '__main__':
    run()
