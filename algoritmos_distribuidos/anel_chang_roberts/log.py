from termcolor import colored

class Logger(object):
    def __init__(self):
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def info(self, id, message):
        color = self._get_color(id)
        print colored("[%s] %s" % (id, message), color)

    def _get_color(self, id):
        return self.colors[ id % 7 ]

