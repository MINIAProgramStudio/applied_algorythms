from Set import Set

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        if not len(matrix) == len(matrix[0]):
            Exception("Matrix is not square")

    def to_lists(self):
        lists = []
        for row in self.matrix:
            lists.append([])
            for i in range(len(row)):
                if row[i]:
                    lists[-1].append(i)
        return lists

    def clear(self):
        self.matrix = [[False]*self.size]*self.size

    def from_lists(self, lists):
        self.size = len(lists)
        new_matrix = [[False]*self.size]*self.size
