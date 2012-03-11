#encoding: utf-8

from algoritmo import Node, NodesFactory

def test_node_precisa_ter_pid_e_link_para_proximo_processo():
    node = Node()
    assert type(node.pid) == long
    assert type(node.next) == Node
    assert node.status == "non-participant"
    assert node.elected_uuid == None

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

def test_node_factory_deve_criar_um_no_linkando_ele_mesmo():
    nodes_factory = NodesFactory()
    node = nodes_factory.build_nodes(1)

    assert node.next == node

