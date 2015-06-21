__author__ = 'ripster'

from ninjabot import bot, config

# Load config
cfg = config.irc.load('config.yaml')

# Start IRC client
bot.run(cfg)
