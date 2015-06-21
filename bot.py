__author__ = 'ripster'

from modules import irc, config


# Load config
cfg = config.load_config('config.yaml')

# Start IRC client
irc.run(cfg)
