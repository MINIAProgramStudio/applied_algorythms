import RandomGraph
import Graph
import UnionFindHandler
import random
import time
import copy
import tqdm
import matplotlib.pyplot as plt
import numpy as np
'''
def kruscal(graph):
    list_of_edges = []
    for row_n in range(len(graph.matrix[0])):
        for column_n in range(row_n, len(graph.matrix[0])):
            if graph.matrix[row_n][column_n] and row_n != column_n:
                list_of_edges.append([graph.matrix[row_n][column_n], row_n, column_n])

    list_of_edges.sort()
    minimal_tree = Graph.WeightedGraph(copy.deepcopy(graph.matrix))
    minimal_tree.matrix[:] = [[None for j in range(len(minimal_tree.matrix))] for i in range(len(minimal_tree.matrix))]

    UF = UnionFindHandler.UnionFindHandler()

    working = True
    counter = 0
    while working:
        edge = list_of_edges[counter]
        vert_1 = edge[1]
        vert_2 = edge[2]
        weight = edge[0]
        if UF.find(vert_1) == UF.find(vert_2):
            if UF.find(vert_1) == -1:
                UF.make_set(vert_1)
                UF.make_set(vert_2)
                UF.union(vert_1, vert_2)
                minimal_tree.add_edge(vert_1, vert_2, weight)
        else:
            if UF.find(vert_1) == -1:
                UF.make_set(vert_1)
                UF.union(vert_1, vert_2)
                minimal_tree.add_edge(vert_1, vert_2, weight)
            elif UF.find(vert_2) == -1:
                UF.make_set(vert_2)
                UF.union(vert_1, vert_2)
                minimal_tree.add_edge(vert_1, vert_2, weight)
        counter += 1
        if UF.universum.keys() == range(0, n_verticies):
            if UF.everything_in_one_set():
                working = False
        if counter >= len(list_of_edges):
            working = False
        return minimal_tree
'''


class SkilledTester:
    def __init__(self):
        pass

    def simple_test(self, n_vertices, probability):
        graph = RandomGraph.RandomWeightedGraph(n_vertices,probability, 0, 1)
        list_of_edges = []
        for row_n in range(len(graph.matrix[0])):
            for column_n in range(row_n, len(graph.matrix[0])):
                if graph.matrix[row_n][column_n] and row_n != column_n:
                    list_of_edges.append([graph.matrix[row_n][column_n],row_n,column_n])

        list_of_edges.sort()
        minimal_tree = Graph.WeightedGraph(copy.deepcopy(graph.matrix))
        minimal_tree.matrix[:] = [[None for j in range(len(minimal_tree.matrix))] for i in range(len(minimal_tree.matrix))]

        if list_of_edges == []:
            return 0

        UF = UnionFindHandler.UnionFindHandler()

        working = True
        counter = 0
        start = time.time()
        while working:
            edge = list_of_edges[counter]
            vert_1 = edge[1]
            vert_2 = edge[2]
            weight = edge[0]
            if UF.find(vert_1) == UF.find(vert_2):
                if UF.find(vert_1) == -1:
                    UF.make_set(vert_1)
                    UF.make_set(vert_2)
                    UF.union(vert_1,vert_2)
                    minimal_tree.add_edge(vert_1,vert_2,weight)
            else:
                if UF.find(vert_1) == -1:
                    UF.make_set(vert_1)
                    UF.union(vert_1, vert_2)
                    minimal_tree.add_edge(vert_1, vert_2, weight)
                elif UF.find(vert_2) == -1:
                    UF.make_set(vert_2)
                    UF.union(vert_1, vert_2)
                    minimal_tree.add_edge(vert_1, vert_2, weight)
            counter += 1
            if UF.universum.keys() == range(0,n_vertices):
                if UF.everything_in_one_set():
                    working = False
            if counter >= len(list_of_edges):
                working = False
        end = time.time()
        return end-start

    def precise_test(self, n_vertices, probability):
        graph = RandomGraph.PreciseRandomWeightedGraph(n_vertices,probability, 0, 1)
        list_of_edges = []
        for row_n in range(len(graph.matrix[0])):
            for column_n in range(row_n, len(graph.matrix[0])):
                if graph.matrix[row_n][column_n] and row_n != column_n:
                    list_of_edges.append([graph.matrix[row_n][column_n],row_n,column_n])

        list_of_edges.sort()
        minimal_tree = Graph.WeightedGraph(copy.deepcopy(graph.matrix))
        minimal_tree.matrix[:] = [[None for j in range(len(minimal_tree.matrix))] for i in range(len(minimal_tree.matrix))]

        if list_of_edges == []:
            return 0

        UF = UnionFindHandler.UnionFindHandler()

        working = True
        counter = 0
        start = time.time()
        while working:
            edge = list_of_edges[counter]
            vert_1 = edge[1]
            vert_2 = edge[2]
            weight = edge[0]
            if UF.find(vert_1) == UF.find(vert_2):
                if UF.find(vert_1) == -1:
                    UF.make_set(vert_1)
                    UF.make_set(vert_2)
                    UF.union(vert_1,vert_2)
                    minimal_tree.add_edge(vert_1,vert_2,weight)
            else:
                if UF.find(vert_1) == -1:
                    UF.make_set(vert_1)
                    UF.union(vert_1, vert_2)
                    minimal_tree.add_edge(vert_1, vert_2, weight)
                elif UF.find(vert_2) == -1:
                    UF.make_set(vert_2)
                    UF.union(vert_1, vert_2)
                    minimal_tree.add_edge(vert_1, vert_2, weight)
            counter += 1
            if UF.universum.keys() == range(0,n_vertices):
                if UF.everything_in_one_set():
                    working = False
            if counter >= len(list_of_edges):
                working = False
        end = time.time()
        return end-start

    def multi_test(self, n_tests, n_vertices, probability):
        total_time = 0
        for i in range(n_tests):
            total_time += self.simple_test(n_vertices,probability)
        return total_time/n_tests

    def multi_test_precise(self, n_tests, n_vertices, probability):
        print(n_vertices)
        total_time = 0
        for i in range(n_tests):
            total_time += self.precise_test(n_vertices,probability)
        return total_time/n_tests




UncleFester = SkilledTester()
'''
fig, ax = plt.subplots()
matrix = []
for n_vertices in tqdm.tqdm(range(10,101,10)):
    matrix.append([])
    for probability in range(0,101,10):
        matrix[-1].append(UncleFester.multi_test(100,n_vertices,probability/100))

im = ax.imshow(matrix)
ax.set_xticks(range(11), labels=range(0,101,10))
ax.set_xlabel("probability")
ax.set_ylabel("vertices")
ax.set_yticks(range(10), labels=range(10,101,10))
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        text = ax.text(j, i, int(matrix[i][j] * 10**7) / 10,
                       ha="center", va="center", color="w")
plt.show()
'''

x = list(range(100,1001))
y = [UncleFester.multi_test_precise(10,i,4000) for i in x]

plt.plot(x, y)
plt.show()