from twisted.internet import reactor, protocol, ssl
from twisted.words.protocols import irc

class Client(irc.IRCClient):
    nickname = "bot"
    operpassword = "ChingChongMotherFucker"
    nickservpass = "mehmehmeh"
    email = "legacy@ratio.ninja"
    registered = "No"

    def signedOn(self):
        self.join(self.factory.channel)
	if self.registered == "No":
	    self.msg("NickServ", "register %s %s" % (self.nickservpass, self.email))
	    self.registered = "Yes"
	elif self.registered == "Yes":
	    self.msg("NickServ", "identify %s" % self.nickservpass)
        self.sendLine("oper %s %s" % (self.nickname, self.operpassword))
        self.msg("OperServ", "login %s" % self.operpassword)
    
    def privmsg(self, user, channel, message):
        user = user.split("!", 1)[0]
        if message.startswith("!help"):
            self.msg(channel, "%s: Help is this way :)" % user)
            self.sendLine("sajoin %s #help" % user)

class Factory(protocol.ClientFactory):
    def __init__(self, channel):
        self.channel = channel
    
    def buildProtocol(self, addr):
       	proto = Client()
        proto.factory = self
        return proto
    
    def clientConnectionLost(self, connector, reason):
        # Try to reconnect if disconnected.
        connector.connect()
    
    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

network = "irc.ratio.ninja"
port = 6697
channel = "rationinja"
reactor.connectSSL(network, port, Factory(channel), ssl.ClientContextFactory())
reactor.run()