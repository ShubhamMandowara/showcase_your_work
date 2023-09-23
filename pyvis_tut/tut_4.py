from pyvis.network import Network
import networkx as nx

if __name__ == '__main__':
    nx_graph = nx.cycle_graph(5)
    net = Network()
    net.from_nx(nx_graph)
    net.write_html('tut_4.html')