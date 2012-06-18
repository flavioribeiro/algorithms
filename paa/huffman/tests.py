from huffman import create_nodes, Node

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


