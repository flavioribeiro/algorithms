#encoding: utf-8

from algoritmo import Node, NodesFactory
import time

def test_node_precisa_ter_pid_e_link_para_proximo_processo():
    node = Node()
    assert type(node.pid) == long
    assert type(node.next) == Node
    assert node.status == "non-participant"
    assert node.elected_pid == None

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

def test_node_precisa_mudar_status_quando_iniciar_eleicao():
    nodes_factory = NodesFactory()
    node = nodes_factory.build_nodes(1)

    def fake_elected(*args):
        pass

    assert node.status == "non-participant"
    node._elected = fake_elected
    node.start_election()
    assert node.status == "participant"

def test_node_precisa_enviar_mensagem_de_eleicao_com_seu_pid():
    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)

    class FakeNode(Node):
        def message(self, msg, called_pid):
            assert called_pid == first_node.pid
            assert msg == "election"

    first_node.next = FakeNode()
    first_node.start_election()

def test_sempre_que_um_node_receber_uma_mensagem_deve_trocar_status_para_participant():
    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)
    first_node.start_election()

    second_node = first_node.next
    third_node = second_node.next

    assert first_node.status == second_node.status == third_node.status == "participant"

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

def test_node_ao_receber_mensagem_de_eleicao_deve_comparar_com_seu_pid_e_se_maior_repassar_msg_com_seu_proprio_pid_se_nao_for_participante_ainda():
    """
    da wikipedia:
        If the UID in the election message is smaller, and the process is not yet a participant, the process replaces the UID in the message with its own UID, sends the updated election message in a clockwise direction.
    """
    def fake_message(msg, pid):
        assert msg == "election"
        assert pid == 200

    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)
    first_node.pid = 100

    second_node = first_node.next
    second_node.pid = 200

    third_node = second_node.next
    third_node.message = fake_message

    first_node.start_election()

def test_node_ao_receber_mensagem_de_eleicao_deve_comparar_com_seu_pid_e_se_maior_e_ja_for_participante_deve_descartar_msg():
    """
    da wikipedia:
      If the UID in the election message is smaller, and the process is already a participant (i.e., the process has already sent out an election message with a UID at least as large as its own UID), the process discards the election message.
    """
    called = [0]
    def fake_message(msg, pid):
        called[0] += 1 # se chamado, ele incrementa 1

    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)
    first_node.pid = 100

    second_node = first_node.next
    second_node.pid = 200
    second_node.status = "participant"

    third_node = second_node.next
    third_node.message = fake_message

    first_node.start_election()

    assert not called[0]

def test_se_o_id_do_node_chegar_de_volta_na_msg_o_no_esta_eleito():
    """
    da wikipedia:
      If the UID in the incoming election message is the same as the UID of the process, that process starts acting as the leader.
    """
    def fake_message(msg, pid):
        called[0] += 1 # se chamado, ele incrementa 1

    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)
    first_node.pid = 100

    second_node = first_node.next
    second_node.pid = 0

    third_node = second_node.next
    third_node.pid = 1

    first_node.start_election()

    assert first_node.elected_pid == first_node.pid
    assert second_node.elected_pid == first_node.pid
    assert third_node.elected_pid == first_node.pid

def test_se_o_node_for_eleito_o_status_dos_nodes_devem_voltar_para_non_participant():
    '''
    TODO verificar se é isso mesmo
    '''
    nodes_factory = NodesFactory()
    first_node = nodes_factory.build_nodes(3)
    first_node.pid = 100

    second_node = first_node.next
    second_node.pid = 0

    third_node = second_node.next
    third_node.pid = 1

    first_node.start_election()

    time.sleep(0.2)
    assert first_node.status == "non-participant" and first_node.elected_pid
    assert second_node.status == "non-participant" and second_node.elected_pid
    assert third_node.status == "non-participant" and third_node.elected_pid


