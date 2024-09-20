import Graph
from random import random

class RandomGraph(Graph.Graph):
    def __init__(self, n_vertices, probability):
        super().__init__([[False]*n_vertices]*n_vertices)
        for row_n in range(self.size):
            for element_n in range(row_n,self.size):
                if random()<probability:
                    self.matrix[row_n][element_n] = True
                    self.matrix[element_n][row_n] = True

class RandomOrientedGraph(Graph.Oriented_Graph):
    def __init__(self, n_vertices, probability):
        super().__init__([[False]*n_vertices]*n_vertices)
        for row_n in range(self.size):
            for element_n in range(self.size):
                if random()<probability:
                    self.matrix[row_n][element_n] = True

class RandomWeightedGraph(Graph.WeightedGraph):
    def __init__(self, n_vertices, probability, min_val, max_val, is_int = False):
        super().__init__([[False] * n_vertices] * n_vertices)
        for row_n in range(self.size):
            for element_n in range(row_n,self.size):
                if random()<probability:
                    weight = random()*(max_val-min_val)+min_val
                    if is_int:
                        weight = int(weight)
                    self.matrix[row_n][element_n] = weight
                    self.matrix[element_n][row_n] = weight

class RandomOrienedWeightedGraph(Graph.OrientedWightedGraph):
    def __init__(self, n_vertices, probability, min_val, max_val, is_int = False):
        super().__init__([[False] * n_vertices] * n_vertices)
        for row_n in range(self.size):
            for element_n in range(self.size):
                if random()<probability:
                    weight = random()*(max_val-min_val)+min_val
                    if is_int:
                        weight = int(weight)
                    self.matrix[row_n][element_n] = weight