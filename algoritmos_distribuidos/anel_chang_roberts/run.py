from algoritmo import NodesFactory

nodes_factory = NodesFactory()
head = nodes_factory.build_nodes(4)
head.start_election()
