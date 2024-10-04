import RandomGraph
import UnionFindHandler
import random
import PythonTableConsole as PTC


class SkilledTester:
    def __init__(self):
        pass

    def simple_test(self, n_verticies, probability):
        graph = RandomGraph.RandomWeightedGraph(n_verticies,probability, 0, 10, True)
        list_of_edges = []
        for row_n in range(len(graph.matrix[0])):
            for column_n in range(row_n, len(graph.matrix[0])):
                if graph.matrix[row_n][column_n]:
                    list_of_edges.append([graph.matrix[row_n][column_n],row_n,column_n])

        table = PTC.PythonTableConsole(graph.matrix)
        print(table)
        print(graph.matrix)

        list_of_edges.sort()
        print(list_of_edges)

graph = RandomGraph.RandomWeightedGraph(5,0.15, 0,1000, True)

print(PTC.PythonTableConsole(graph.matrix))