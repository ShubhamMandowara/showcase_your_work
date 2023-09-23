from pyvis.network import Network


if __name__ == '__main__':
    net = Network()
    net.add_node('A', label='A')
    net.add_node('B', label='B')

    net.add_edge('A', 'B', physics=False, title='Edge', arrowStrikethrough=False, )
    net.write_html('tut_1.html')
    