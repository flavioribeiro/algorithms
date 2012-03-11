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

#def test_node_precisa_mudar_status_quando_iniciar_eleicao():
#    nodes_factory = NodesFactory()
#    node = nodes_factory.build_nodes(1)
#
#    assert node.status == "non-participant"
#    node.start_election()
#    assert node.status == "participant"
#
def test_node_precisa_enviar_mensagem_de_eleicao_com_seu_pid():
    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)

    class FakeNode(Node):
        def message(self, msg, called_pid):
            assert called_pid == first_node.pid
            assert msg == "election"

    first_node.next = FakeNode()
    first_node.start_election()

#def test_sempre_que_um_node_receber_uma_mensagem_deve_trocar_status_para_participant():
#    nodes_factory = NodesFactory()
#    first_node = nodes_factory.build_nodes(3)
#    first_node.start_election()
#
#    second_node = first_node.next
#    third_node = second_node.next
#
#    assert first_node.status == second_node.status == third_node.status == "participant"
#
def test_node_ao_receber_mensagem_de_eleicao_deve_comparar_com_seu_pid_e_repassar_pid_se_menor():
    """
    da wikipedia:
      If the UID in the election message is larger, the process unconditionally forwards the election message in a clockwise direction.
   """
    def fake_message(msg, pid):
        assert msg == "election"
        assert pid == 100

    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)
    first_node.pid = 100

    second_node = first_node.next
    second_node.pid = 0

    third_node = second_node.next
    third_node.message = fake_message

    first_node.start_election()

