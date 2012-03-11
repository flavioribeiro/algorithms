#encoding: utf-8

import uuid

class NodesFactory(object):
    def build_nodes(self, qty):
        new_node = Node()
        first_node = new_node
        previous_node = first_node
        previous_node.next = first_node

        for i in range(qty-1):
            new_node = Node()
            previous_node.next = new_node
            previous_node = new_node

        new_node.next = first_node
        return first_node

class Node(object):
    def __init__(self):
        self.pid = self._build_pid()
        self.next = self # se apenas um nó for criado, ele é linkado nele mesmo
        self.status = "non-participant"
        self.elected_uuid = None

    def start_election(self):
        self.status = "participant"
        self.next.message("election", self.pid)

    def message(self, msg, called_pid):
        self.next.message(msg, called_pid)
        self.status = "participant"

    def _build_pid(self):
        return uuid.uuid4().int

