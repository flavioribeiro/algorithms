
class Node(object):
    def __init__(self):
        self.pid = self._cria_pid()
        self.next = self

    def _cria_pid(self):
        return 1

