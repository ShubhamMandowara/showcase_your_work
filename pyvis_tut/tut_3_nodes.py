from pyvis.network import Network


if __name__ == '__main__':
    net = Network()
    net.add_nodes([1, 2, 3], value=[10, 100, 200], 
                  title=['Node 1', 'Node 2', 'Node 3'], 
                  x= [10, 20, 30], 
                  y=[100, 200, 300],
                  label = ['NODE 1', 'NODE 2', 'NODE 3'],
                   color = ['green', 'red', 'yellow'] )
    
    net.write_html('tut-3.html')