class Node(object):
  def __init__(self, weight, symbol=None, right_node=None, left_node=None):
    self.weight = weight
    self.symbol = symbol
    self.right_node = right_node
    self.left_node = left_node

  def is_leaf(self):
    return not self.right_node and not self.left_node

def create_tree(symbols):
  nodes = create_nodes(symbols)
  ordered_nodes = nodes.sort(node_cmp)

def create_nodes(symbols):
  return [Node(symbol[1], symbol[0]) for symbol in symbols.items()]

def node_cmp(node1, node2):
#TODO write tests
  if node1.weight > node2.weight:
    return 1
  elif node1.weight < node2.weight:
    return -1
  else:
    return 0
