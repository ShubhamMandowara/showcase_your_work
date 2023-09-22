from pyvis.network import Network


if __name__ == '__main__':
    net = Network()
    net.add_node('A', label='A')
    net.add_node('B', label='B')
    net.add_edge('A','B', value=10, arrowStrikethrough=False, physics=False, title='Edge')
    net.write_html('index.html')