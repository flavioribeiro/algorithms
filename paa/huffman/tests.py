from huffman import create_nodes, Node, node_cmp, create_tree, create_bits_reprs

def test_huffman_create_nodes_should_create_objects_from_symbols():
  symbols = {10: 'a', 18: 'b'}
  nodes = create_nodes(symbols)

  for node in nodes:
    assert isinstance(node, Node)
    assert node.is_leaf()

def test_huffman_node_cmp_should_sort_nodes_according_to_weight():
  symbols = {10: 'a', 18: 'b', 200: 'c', 1: 'd', 60: 'e'}
  nodes = create_nodes(symbols)
  nodes.sort(node_cmp)

  assert ['c', 'e', 'b', 'a', 'd'] == [node.symbol for node in nodes]

def test_huffman_create_tree_should_create_root_linked_to_two_nodes():
  symbols = {10: 'a', 18: 'b'}
  root_node = create_tree(symbols)

  assert False == root_node.is_leaf()
  assert 28 == root_node.weight
  assert 'a' == root_node.right_node.symbol
  assert 'b' == root_node.left_node.symbol

def test_huffman_create_tree_with_just_one_node_should_return_itself():
  symbols = {10: 'a'}
  root_node = create_tree(symbols)

  assert True == root_node.is_leaf()
  assert 10 == root_node.weight
  assert 'a' == root_node.symbol

def test_huffman_should_create_a_big_tree():
# The tree should be:
#          (root)
#         /      \
#  (a+d+e+f)     (b+c)
#   /     \      /   \
# (a)  (d+e+f) (b)   (c)
#      /    \
#    (d)   (e+f)
#          /   \
#        (e)   (f)

  symbols = {6: 'a', 5: 'b', 4: 'c', 3: 'd',  2: 'e', 1: 'f'}
  root = create_tree(symbols)

  assert sum(symbols.keys()) == root.weight
  assert "c" == root.right_node.right_node.symbol
  assert "b" == root.right_node.left_node.symbol
  assert "a" == root.left_node.left_node.symbol
  assert "d" == root.left_node.right_node.left_node.symbol
  assert "e" == root.left_node.right_node.right_node.left_node.symbol
  assert "f" == root.left_node.right_node.right_node.right_node.symbol

def test_huffman_create_bits_reprs_should_return_a_dict_with_symbols_and_reprs():
  symbols = {10: "a", 20: "b"}
  reprs = create_bits_reprs(symbols)

  assert {"a": "00",  "b": "01"} == reprs

