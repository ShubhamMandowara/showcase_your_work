from pyvis.network import Network

if __name__ == '__main__':
    net = Network()
    net.add_node('Shoes', label='Shoes', color='green', size=100, shape='ellipse')
    net.add_node('Nike', label='Nike', color='black')
    net.add_edge('Shoes', 'Nike')
    net.write_html('tut-2.html')