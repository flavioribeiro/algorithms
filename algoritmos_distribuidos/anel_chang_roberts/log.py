from termcolor import colored
from random import choice

class Logger(object):
    def __init__(self):
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def info(self, id, message):
        color = self._get_color(id)
        attrs = []
        if "Yeah" in message:
            attrs = ['bold', 'dark']

        print colored("[%s] %s" % (id, message), color, attrs=attrs)
    def _get_color(self, id):
        return self.colors[ id % 7 ]

