from Set import Set

class Graph:
    '''
    Non-oriented graph wihout weights
    '''
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        if not len(matrix) == len(matrix[0]):
            Exception("Matrix is not square")

    def to_lists(self):
        lists = []
        for row in self.matrix:
            lists.append([])
            for element_n in range(len(row)):
                if row[element_n]:
                    lists[-1].append(element_n)
        return lists

    def clear(self):
        self.matrix = [[False]*self.size]*self.size
        return 0

    def from_lists(self, lists):
        self.size = len(lists)
        new_matrix = [[False]*self.size]*self.size
        for list_n in range(len(lists)):
            for i in range(len(lists[list_n])):
                new_matrix[list_n][i] = True
        self.matrix = new_matrix
        return 0

    def add_vertice(self, repeat = 1):
        for i in range(repeat):
            self.size+=1
            for row_n in range(len(self.matrix)):
                self.matrix[row_n].append(False)
            self.matrix.append([False]*self.size)

    def add_edge(self, start, stop):
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

