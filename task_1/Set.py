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
