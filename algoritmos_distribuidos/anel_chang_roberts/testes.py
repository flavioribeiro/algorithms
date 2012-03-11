#encoding: utf-8

from algoritmo import Node, NodesFactory

def test_node_precisa_ter_pid_e_link_para_proximo_processo():
    node1 = Node()
    assert type(node1.pid) == long
    assert type(node1.next) == Node

def test_nodes_precisam_ter_pids_unicos():
    pids = []
    for i in range(1000):
        node = Node()
        pids.append(node.pid)

    assert not [pid for pid in pids if pids.count(pid) > 1]

def test_links_dos_nodes_devem_criar_um_anel():
    nodes_factory = NodesFactory()

    first_node = nodes_factory.build_nodes(3)
    second_node = first_node.next
    third_node = second_node.next

    assert first_node.next == second_node
    assert second_node.next == third_node
    assert third_node.next == first_node

