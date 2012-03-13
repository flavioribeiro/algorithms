from algoritmo import NodesFactory
import sys

nodes_factory = NodesFactory()
head = nodes_factory.build_nodes(int(sys.argv[1]))
head.start_election()
