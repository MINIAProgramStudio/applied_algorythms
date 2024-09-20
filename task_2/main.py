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
            y_axis.append((stop-start)*10**3/n_tests)
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
            y_axis.append((stop - start) * 10 ** 3 / n_tests)
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
            y_axis.append((stop - start) * 10 ** 3)
        return (x_axis, y_axis)

    def ll(self, n_tests, ver_start, ver_stop, ver_step, pr_start, pr_stop, pr_step):
        y_axis = [i for i in range(ver_start,ver_stop, ver_step)]
        x_axis = [i for i in range(pr_start,pr_stop,pr_step)]
        time_map_to = []
        time_map_from = []
        for ver_n in tqdm(range(ver_start, ver_stop, ver_step)):
            time_map_to.append([])
            time_map_from.append([])
            for pr in range(pr_start,pr_stop,pr_step):
                graphs = []
                for i in range(n_tests):
                    graphs.append(RandomGraph.RandomGraph(ver_n,pr/100))
                temp = []
                start = time.time()
                for graph in graphs:
                    temp.append(graph.to_ll())
                stop = time.time()
                time_map_to[-1].append((stop - start) * 10 ** 3)
                start = time.time()
                for graph_n in range(len(graphs)):
                    graphs[graph_n].from_ll(temp[graph_n])
                stop = time.time()
                time_map_from[-1].append((stop - start) * 10 ** 3)
        return (x_axis, y_axis, time_map_to, time_map_from)



UncleFester = SkilledTester()

'''
result = UncleFester.graph_new_vertice(1000,1,1000, 10)
plt.plot(result[0],result[1])
plt.show()


result = UncleFester.graph_new_edge(100,1,1000, 10)
plt.plot(result[0],result[1])
plt.show()

result = UncleFester.graph_delete_vertice(1000,1000,1, -1)
plt.plot(result[0],result[1])
plt.show()
'''
fig, ax = plt.subplots()
result = UncleFester.ll(100,10,100,10,0,101,10)
im = ax.imshow(result[2])
ax.set_xticks(range(len(result[0])), labels=result[0])
ax.set_xlabel("probability")
ax.set_ylabel("vertices")
ax.set_yticks(range(len(result[1])), labels=result[1])
for i in range(len(result[2])):
    for j in range(len(result[2][0])):
        text = ax.text(j, i, int(result[2][i][j] * 10) / 10,
                       ha="center", va="center", color="w")
plt.show()

fig, ax = plt.subplots()
im = ax.imshow(result[2])
ax.set_xticks(range(len(result[0])), labels=result[0])
ax.set_xlabel("probability")
ax.set_ylabel("vertices")
ax.set_yticks(range(len(result[1])), labels=result[1])
for i in range(len(result[2])):
    for j in range(len(result[2][0])):
        text = ax.text(j, i, int(result[3][i][j] * 10) / 10,
                       ha="center", va="center", color="w")
plt.show()