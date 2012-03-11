#encoding: utf-8

import uuid

class NodesFactory(object):
    def build_nodes(self, qty):
        first_node = Node()
        previous_node = first_node
        nodes = [previous_node]

        for i in range(qty-1):
            new_node = Node()
            previous_node.next = new_node
            previous_node = new_node
            nodes.append(previous_node)

        new_node.next = first_node

        return nodes

class Node(object):
    def __init__(self):
        self.pid = self._build_pid()
        self.next = self # se apenas um nó for criado, ele é linkado nele mesmo

    def _build_pid(self):
        return uuid.uuid4().int
