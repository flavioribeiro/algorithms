class Node(object):
  def __init__(self, weight, symbol=None, right_node=None, left_node=None):
    self.weight = weight
    self.symbol = symbol
    self.right_node = right_node
    self.left_node = left_node

  def is_leaf(self):
    return not self.right_node and not self.left_node

  def set_repr(self, representation):
    self.representation = representation

def create_tree(symbols):
  nodes = create_nodes(symbols)
  nodes.sort(node_cmp)

  while nodes:
    node_1 = nodes.pop()
    if nodes:
      node_2 = nodes.pop()
      link_node = make_link_node(node_1, node_2)
      nodes.append(link_node)
      nodes.sort(node_cmp)
    else:
      link_node = node_1

  return link_node

def create_bits_reprs(symbols):
  root = create_tree(symbols)
  set_representations("", root)
  representations = {}
  get_representations(root, representations)

  return representations

def get_representations(node, representations):
  if node.is_leaf():
    representations[node.symbol] = node.representation
  else:
    get_representations(node.right_node, representations)
    get_representations(node.left_node, representations)

def set_representations(representation, node):
  if node.is_leaf():
    node.representation = representation
  else:
    set_representations(representation + "1", node.right_node)
    set_representations(representation + "0", node.left_node)

def make_link_node(node_1, node_2):
  total_weight = node_1.weight + node_2.weight
  return  Node(weight=total_weight, right_node=node_1, left_node=node_2)

def create_nodes(symbols):
  return [Node(symbol[0], symbol[1]) for symbol in symbols.items()]

def node_cmp(node1, node2):
  if node1.weight < node2.weight:
    return 1
  elif node1.weight > node2.weight:
    return -1
  else:
    return 0
