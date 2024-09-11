import copy

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    value = None
    next_node = None

class Set:
    def __init__(self, values = []):
        for value in values:
            self.insert(value)

    first_node = None

    def insert(self, value):
        if self.first_node is None:
            self.first_node = Node(value)
            return 0

        if value < self.first_node.value:
            new_node = Node(value, self.first_node)
            self.first_node = new_node
            return 0

        if value == self.first_node.value:
            return -1

        selected_node = self.first_node
        while True:
            if selected_node.next_node is None:
                new_node = Node(value)
                selected_node.next_node = new_node
                return 0
            if selected_node.next_node.value == value:
                return -1
            elif value < selected_node.next_node.value:
                new_node = Node(value, selected_node.next_node)
                selected_node.next_node = new_node
                return 0
            selected_node = selected_node.next_node

    def __str__(self):
        output = []
        selected_node = self.first_node
        while True:
            output.append(selected_node.value)
            if selected_node.next_node is None:
                return str(output)
            else:
                selected_node = selected_node.next_node

    def delete(self, value):
        if value < self.first_node.value:
            return -1
        if value == self.first_node.value:
            self.first_node = self.first_node.next_node

        selected_node = self.first_node
        while True:
            if selected_node.next_node is None:
                return -1
            elif selected_node.next_node.value == value:
                selected_node.next_node = selected_node.next_node.next_node
                return 0
            else:
                selected_node = selected_node.next_node

    def search(self, value):
        if self.first_node is None:
            return -1
        if value < self.first_node.value:
            return -1

        selected_node = self.first_node
        counter = 0
        while True:
            if value == selected_node:
                return counter
            elif selected_node.next_node is None:
                return -1
            else:
                selected_node = selected_node.next_node

    def clear(self):
        self.first_node = None
        return 0

    def __add__(self, other): # Union
        if self.first_node is None:
            if other.first_node is None:
                return Set()
            else:
                return copy.deepcopy(other)
        elif other.first_node is None:
            if self.first_node is None:
                return Set()
            else:
                return copy.deepcopy(self)

        new_set = Set()
        node_a = self.first_node
        node_b = other.first_node
        if node_a.value > node_b.value:
            new_set.insert(node_b.value)
            node_b = node_b.next_node
        else:
            new_set.insert(node_a.value)
            node_a = node_a.next_node
        node_n = new_set.first_node
        while True:
            if node_a is None:
                while not node_b is None:
                    node_n.next_node = Node(node_b.value)
                    node_b = node_b.next_node
            elif node_b is None:
                while not node_a is None:
                    node_n.next_node = Node(node_a.value)
                    node_a = node_a.next_node

            if node_a.value > node_b.value:
                node_n.next_node = Node(node_b.value)
                node_b = node_b.next_node
                node_n = node_n.next_node
            else:
                node_n.next_node = Node(node_a.value)
                node_a = node_a.next_node
                node_n = node_n.next_node

    def __mul__(self, other): # Intersection
        if self.first_node is None:
            return Set()
        elif other.first_node is None:
            return Set()

        new_set = Set()
        node_a = self.first_node
        node_b = other.first_node

        # multiply to get first element
        while new_set.first_node is None:
            if node_a.value == node_b.value:
                new_set.first_node = Node(node_a.value)
                node_a = node_a.next_node
                node_b = node_b.next_node
                if node_b is None or node_a is None:
                    return new_set
            else:
                if node_a.value > node_b.value:
                    node_b = node_b.next_node
                    if node_b is None:
                        return new_set
                else:
                    node_a = node_a.next_node
                    if node_a is None:
                        return new_set

        node_n = new_set.first_node
        # multiply to get other elements
        while True:
            if node_a.value == node_b.value:
                node_n.next_node = Node()
                node_a = node_a.next_node
                node_b = node_b.next_node
                if node_b is None or node_a is None:
                    return new_set
            else:
                if node_a.value > node_b.value:
                    node_b = node_b.next_node
                    if node_b is None:
                        return new_set
                else:
                    node_a = node_a.next_node
                    if node_a is None:
                        return new_set

    def __sub__(self, other): # SetDifference
        if self.first_node is None:
            return Set()
        elif other.first_node is None:
            return copy.deepcopy(self)

        node_a = self.first_node
        node_b = other.first_node
        new_set = Set()

        # subtract to get first element
        while new_set.first_node is None:
            if node_a.value == node_b.value:
                node_a = node_a.next_node
                node_b = node_b.next_node
                if node_b is None or node_a is None:
                    return new_set
            else:
                if node_a.value > node_b.value:
                    node_b = node_b.next_node
                    if node_b is None:
                        return copy.deepcopy(self)
                else:
                    new_set.first_node = Node(node_a.value)
                    node_a = node_a.next_node
                    if node_a is None:
                        return new_set

        node_n = new_set.first_node
        # subtract to get other elements
        while True:
            if node_a.value == node_b.value:
                node_a = node_a.next_node
                node_b = node_b.next_node
                if node_b is None or node_a is None:
                    return new_set
            else:
                if node_a.value > node_b.value:
                    node_b = node_b.next_node
                    if node_b is None:
                        while node_a is not None:
                            node_n.next_node = Node(node_a.value)
                            node_n = node_n.next_node
                            node_a = node_a.next_node
                        return new_set
                else:
                    node_n.next_node = Node(node_a.value)
                    node_n = node_n.next_node
                    node_a = node_a.next_node
                    if node_a is None:
                        return new_set

    def __truediv__(self, other): #SymDifference
        if self.first_node is None:
            return copy.deepcopy(other)
        elif other.first_node is None:
            return copy.deepcopy(self)

        node_a = self.first_node
        node_b = other.first_node
        new_set = Set()

        # sym_subtract to get first element
        while new_set.first_node is None:
            if node_a.value == node_b.value:
                node_a = node_a.next_node
                node_b = node_b.next_node
                if node_b is None or node_a is None:
                    return new_set
            else:
                if node_a.value > node_b.value:
                    new_set.first_node = Node(node_b.value)
                    node_b = node_b.next_node
                else:
                    new_set.first_node = Node(node_a.value)
                    node_a = node_a.next_node

        node_n = new_set.first_node
        # sym_subtract to get other elements (up to the end of one of the sets)
        while True:
            if node_a.value == node_b.value:
                node_a = node_a.next_node
                node_b = node_b.next_node
                if node_b is None or node_a is None:
                    return new_set
            else:
                if node_a.value > node_b.value:
                    new_set.first_node = Node(node_b.value)
                    node_b = node_b.next_node
                    if node_b is None:
                        break
                else:
                    node_n.next_node = Node(node_a.value)
                    node_n = node_n.next_node
                    node_a = node_a.next_node
                    if node_a is None:
                        break

        if node_a is None:
            while not node_b is None:
                node_n.next_node = Node(node_b.value)
                node_n = node_n.next_node
                node_b = node_b.next_node
        elif node_b is None:
            while not node_a is None:
                node_n.next_node = Node(node_a.value)
                node_n = node_n.next_node
                node_a = node_a.next_node

        return new_set

    def __len__(self):
        if self.first_node is None:
            return 0
        counter = 1
        selected_node = self.first_node
        while not selected_node is None:
            selected_node = selected_node.next_node
            counter+=1
        return counter

    def to_list(self):
        selected_node = self.first_node
        output_list = []
        while not selected_node is None:
            output_list.append(selected_node.value)
            selected_node = selected_node.next_node
        return output_list

