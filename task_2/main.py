import Graph
import RandomGraph
from random import random
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

class SkilledTester:
    def __init__(self):
        pass

    def graph_new_vertice(self, n_tests, ver_start, ver_stop, ver_step=1, probaility=0.5):
        graphs = []
        x_axis = [i for i in range(ver_start, ver_stop+1, ver_step)]
        y_axis = []
        for i in range(n_tests):
            graphs.append(RandomGraph.RandomGraph(ver_start,probaility))
        for i in tqdm(range(ver_start,ver_stop+1,ver_step)):
            start = time.time()
            for graph in graphs:
                graph.add_vertice(ver_step)
            stop = time.time()
            y_axis.append((stop-start)*10**6/n_tests)
        return(x_axis,y_axis)

    def graph_new_edge(self, n_tests, ver_start, ver_stop, ver_step=1, probaility=0.5):

        x_axis = [i for i in range(ver_start, ver_stop + 1, ver_step)]
        y_axis = []
        for ver in tqdm(range(ver_start, ver_stop + 1, ver_step)):
            graphs = []
            for i in range(n_tests):
                graphs.append(RandomGraph.RandomGraph(ver, probaility))
            start = time.time()
            for graph in graphs:
                for i in range(n_tests):
                    graph.add_edge(int(random()*ver),int(random()*ver))
            stop = time.time()
            y_axis.append((stop - start) * 10 ** 6 / n_tests)
        return (x_axis, y_axis)

    def graph_delete_vertice(self, n_tests, ver_start, ver_stop, ver_step=-1, probaility=0.5):
        x_axis = [i for i in range(ver_start, ver_stop, ver_step)]
        y_axis = []
        graphs = []
        for i in tqdm(range(n_tests)):
            graphs.append(RandomGraph.RandomGraph(ver_start, probaility))
        for ver in tqdm(range(ver_start, ver_stop, ver_step)):
            start = time.time()
            for graph in graphs:
                for i in range(ver_step):
                    graph.remove_edge(int(random() * (ver-i)))
            stop = time.time()
            y_axis.append((stop - start) * 10 ** 6)
        return (x_axis, y_axis)


UncleFester = SkilledTester()


result = UncleFester.graph_new_vertice(1000,1,1000, 10)
plt.plot(result[0],result[1])
plt.show()


result = UncleFester.graph_new_edge(100,1,1000, 10)
plt.plot(result[0],result[1])
plt.show()

result = UncleFester.graph_delete_vertice(1000,1000,1, -1)
plt.plot(result[0],result[1])
plt.show()