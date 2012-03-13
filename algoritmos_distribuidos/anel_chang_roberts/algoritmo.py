#encoding: utf-8

import uuid
from log import Logger

logger = Logger()

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
        self.status = None
        self.elected_pid = None
        self.next = self # se apenas um nó for criado, ele é linkado nele mesmo
        logger.info(self.pid, "initialized")
        self._change_status("non-participant")

    def start_election(self):
        self._change_status("participant")
        logger.info(self.pid, "starting election")
        self.next.message("election", self.pid)

    def message(self, msg, called_pid):
        logger.info(self.pid, "got a message -> %s" % msg)
        if msg == "election":
            self._verify_election(called_pid)

        elif msg == "elected" and not self.elected_pid:
            self._elected(called_pid)

    def _verify_election(self, called_pid):
        if self.status == "non-participant":
            self._change_status("participant")
            self.next.message("election", max(self.pid, called_pid))

        elif called_pid == self.pid:
            logger.info(self.pid, "Yeah, i've won the election! :-)")
            self._elected(self.pid)

    def _elected(self, pid):
        self.elected_pid = pid
        self._change_status("non-participant")
        self.next.message("elected", self.elected_pid)

    def _change_status(self, new_status):
        logger.info(self.pid, "Changing status: %s -> %s" % (self.status, new_status))
        self.status = new_status

    def _build_pid(self):
        return uuid.uuid4().int

