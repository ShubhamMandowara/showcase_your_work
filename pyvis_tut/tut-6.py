from pyvis.network import Network
import networkx as nx

if __name__ == '__main__':
    graph_nx = nx.complete_graph(5)
    net = Network(select_menu=True)
    net.from_nx(graph_nx)
    net.write_html('tut-6.html')