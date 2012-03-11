
import uuid

class Node(object):
    def __init__(self):
        self.pid = self._cria_pid()
        self.next = self

    def _cria_pid(self):
        return uuid.uuid4().int

