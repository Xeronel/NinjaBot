__author__ = 'ripster'

import yaml


class Config:
    def __init__(self, file_name):
        self.conf = None
        with open(file_name, 'r') as f:
            self.conf = yaml.load(f.read())

    def print_config(self):
        print(self.conf)