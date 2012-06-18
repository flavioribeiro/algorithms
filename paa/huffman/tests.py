from huffman import create_nodes, Node, node_cmp

#def test_huffman_create_tree_should_create_root_linked_to_two_nodes():
  #symbols = {10: 'a', 18: 'b'}
  #root_node = create_tree(symbols)
#
  #assert False == root_node.is_leaf
  #assert 28 == root_node.weight
  #assert 'a' == root_node.right_node.symbol
  #assert 'b' == root_node.left_node.symbol

def test_huffman_create_nodes_should_create_objects_from_symbols():
  symbols = {10: 'a', 18: 'b'}
  nodes = create_nodes(symbols)

  for node in nodes:
    assert isinstance(node, Node)

def test_huffman_node_cmp_should_sort_nodes_according_to_weight():
  symbols = {10: 'a', 18: 'b', 200: 'c', 1: 'd', 60: 'e'}
  nodes = create_nodes(symbols)
  nodes.sort(node_cmp)

  assert ['c', 'e', 'b', 'a', 'd'] == [node.symbol for node in nodes]
