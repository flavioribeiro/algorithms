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
        self.elected_pid = None

    def start_election(self):
        self.status = "participant"
        self.next.message("election", self.pid)

    def message(self, msg, called_pid):
        if msg == "election":
            if self.status == "non-participant":
                self.next.message(msg, max(self.pid, called_pid))

            elif called_pid == self.pid and not self.elected_pid:
                self._elected(self.pid)

        elif msg == "elected" and not self.elected_pid:
            self._elected(called_pid)

        self.status = "participant"

    def _elected(self, pid):
        self.elected_pid = pid
        self.next.message("elected", self.elected_pid)

    def _build_pid(self):
        return uuid.uuid4().int

