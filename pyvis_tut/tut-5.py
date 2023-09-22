from pyvis.network import Network
import networkx as nx


if __name__ == '__main__':
    nx_graph = nx.cycle_graph(5)
    net = Network(height='100%', width='100%', bgcolor = '#222222', font_color='while', select_menu=True )
    net.from_nx(nx_graph)
    net.write_html('tut-5.html')