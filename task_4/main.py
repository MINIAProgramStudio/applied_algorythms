import RandomGraph
import UnionFindHandler

class SkilledTester:
    def __init__(self):
        pass

    def simple_test(self, n_verticies, probability):
        graph = RandomGraph.RandomWeightedGraph(n_verticies,probability, 0, 1)
        list_of_edges = []
        for row_n in range(len(graph.matrix)):
            for column_n in range(row_n+1, len(graph.matrix)):
                if graph.matrix[row_n][column_n]:
                    list_of_edges.append([graph.matrix[row_n][column_n],row_n,column_n])


        #list_of_edges.sort()
        #print(list_of_edges)



UncleFester = SkilledTester()

UncleFester.simple_test(10,0.05)