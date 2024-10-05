import Graph
from random import random
import copy

class RandomGraph(Graph.Graph):
    def __init__(self, n_vertices, probability):
        start_row = [False] * n_vertices
        y = []
        for i in range(n_vertices):
            y.append(copy.deepcopy(start_row))
        super().__init__(y)
        for row_n in range(self.size):
            for element_n in range(row_n,self.size):
                if random()<probability:
                    self.matrix[row_n][element_n] = True
                    self.matrix[element_n][row_n] = True

class RandomOrientedGraph(Graph.Oriented_Graph):
    def __init__(self, n_vertices, probability):
        start_row = [False] * n_vertices
        y = []
        for i in range(n_vertices):
            y.append(copy.deepcopy(start_row))
        super().__init__(y)
        for row_n in range(self.size):
            for element_n in range(self.size):
                if random()<probability:
                    self.matrix[row_n][element_n] = True

class RandomWeightedGraph(Graph.WeightedGraph):
    def __init__(self, n_vertices, probability, min_val, max_val, is_int = False):
        start_row = [None] * n_vertices
        y = []
        for i in range(n_vertices):
            y.append(copy.deepcopy(start_row))
        super().__init__(y)
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
        start_row = [None] * n_vertices
        y = []
        for i in range(n_vertices):
            y.append(copy.deepcopy(start_row))
        super().__init__(y)
        for row_n in range(self.size):
            for element_n in range(self.size):
                if random()<probability:
                    weight = random()*(max_val-min_val)+min_val
                    if is_int:
                        weight = int(weight)
                    self.matrix[row_n][element_n] = weight

class PreciseRandomWeightedGraph(Graph.WeightedGraph):
    def __init__(self, n_vertices, probability, min_val, max_val, is_int = False):
        start_row = [None] * n_vertices
        y = []
        for i in range(n_vertices):
            y.append(copy.deepcopy(start_row))
        super().__init__(y)
        counter = 0
        while counter < probability:
            row_n = int(random()*n_vertices)
            element_n = int(random()*n_vertices)
            if self.matrix[row_n][element_n] is None:
                weight = random()*(max_val-min_val)+min_val
                if is_int:
                    weight = int(weight)
                self.matrix[row_n][element_n] = weight
                self.matrix[element_n][row_n] = weight
                counter+=1