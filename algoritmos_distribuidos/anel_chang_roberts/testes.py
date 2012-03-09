#encoding: utf-8

from algoritmo import Node

def test_node_precisa_ter_pid_e_proximo_processo():
    node1 = Node()
    assert type(node1.pid) == int
    assert type(node1.next) == Node



