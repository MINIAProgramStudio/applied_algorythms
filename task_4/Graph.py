from LinkedList import LinkedList

class Graph:
    '''
    Non-oriented graph wihout weights
    '''
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        if not len(matrix) == len(matrix[0]):
            Exception("Matrix is not square")

    def to_ll(self):
        lists = []
        for row in self.matrix:
            lists.append(LinkedList())
            for element_n in range(len(row)):
                if row[element_n]:
                    lists[-1].insert(element_n)
        return lists

    def clear(self):
        self.matrix = [[False]*self.size]*self.size
        return 0

    def from_ll(self, lists):
        self.size = len(lists)
        new_matrix = [[False]*self.size]*self.size
        for list_n in range(len(lists)):
            selected_node = lists[list_n].first_node
            while selected_node is not None:
                new_matrix[list_n][selected_node.value] = True
                selected_node = selected_node.next_node
        self.matrix = new_matrix
        return 0

    def add_vertice(self, repeat = 1):
        for i in range(repeat):
            self.size+=1
            for row_n in range(len(self.matrix)):
                self.matrix[row_n].append(False)
            self.matrix.append([False]*self.size)
        return 0

    def add_edge(self, start, stop, weight=0):
        self.matrix[start][stop] = True
        self.matrix[stop][start] = True
        return 0

    def remove_vertice(self, index):
        if index >= self.size:
            return -1

        for row_n in range(self.size):
            self.matrix[row_n].pop(index)
        self.matrix.pop(index)
        return 0

    def remove_edge(self, start, stop):
        self.matrix[start][stop] = False
        self.matrix[stop][start] = False
        return 0


class Oriented_Graph(Graph):
    '''
    Oriented graph. Based on Graph class
    '''
    def add_edge(self, start, stop, weight=0):
        self.matrix[start][stop] = True
        return 0

    def remove_edge(self, start, stop):
        self.matrix[start][stop] = False
        return 0

class WeightedGraph(Graph):
    '''
    Non-oriented weighted graph
    '''
    def to_ll(self):
        lists = []
        for row in self.matrix:
            lists.append(LinkedList())
            for element_n in range(len(row)):
                if row[element_n]:
                    lists[-1].insert((element_n, row[element_n]))
        return lists

    def from_ll(self, lists):
        self.size = len(lists)
        new_matrix = [[0] * self.size] * self.size
        for list_n in range(len(lists)):
            selected_node = lists[list_n].first_node
            while selected_node is not None:
                new_matrix[list_n][selected_node.value[0]] = selected_node.value[1]
                selected_node = selected_node.next_node
        self.matrix = new_matrix
        return 0

    def clear(self):
        self.matrix = [[0]*self.size]*self.size
        return 0

    def add_vertice(self, repeat = 1):
        for i in range(repeat):
            self.size+=1
            for row_n in range(len(self.matrix)):
                self.matrix[row_n].append(0)
            self.matrix.append([0]*self.size)
        return 0

    def add_edge(self, start, stop, weight=0):
        self.matrix[start][stop] = weight
        self.matrix[stop][start] = weight
        return 0

    def remove_edge(self, start, stop):
        self.matrix[start][stop] = 0
        self.matrix[stop][start] = 0
        return 0

class OrientedWightedGraph(WeightedGraph):
    '''
    Oriented weighted graph
    '''
    def add_edge(self, start, stop, weight=0):
        self.matrix[start][stop] = weight
        return 0

    def remove_edge(self, start, stop):
        self.matrix[start][stop] = 0
        return 0