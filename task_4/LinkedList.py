import copy





class LinkedList:
    class _Node:
        def __init__(self, value, next_Node=None):
            self.value = value
            self.next_Node = next_Node

        value = None
        next_Node = None
    def __init__(self, values=[]):
        for value in values:
            self.insert(value)

    first_Node = None

    def insert(self, value):
        if self.first_Node is None:
            self.first_Node = self._Node(value)
            return 0

        if value == self.first_Node.value:
            return -1

        selected_Node = self.first_Node
        while not selected_Node is None:
            if selected_Node.value == value:
                return -1
            selected_Node = selected_Node.next_Node
        new_Node = self._Node(value, self.first_Node)
        self.first_Node = new_Node

    def __str__(self):
        output = []
        selected_Node = self.first_Node
        while True:
            output.append(selected_Node.value)
            if selected_Node.next_Node is None:
                return str(output)
            else:
                selected_Node = selected_Node.next_Node

    def delete(self, value):
        if self.first_Node is None:
            return -1
        if value == self.first_Node.value:
            self.first_Node = self.first_Node.next_Node

        selected_Node = self.first_Node
        while True:
            if selected_Node.next_Node is None:
                return -1
            elif selected_Node.next_Node.value == value:
                selected_Node.next_Node = selected_Node.next_Node.next_Node
                return 0
            else:
                selected_Node = selected_Node.next_Node

    def search(self, value):
        if self.first_Node is None:
            return -1

        selected_Node = self.first_Node
        counter = 0
        while True:
            if value == selected_Node:
                return counter
            elif selected_Node.next_Node is None:
                return -1
            else:
                selected_Node = selected_Node.next_Node

    def clear(self):
        self.first_Node = None
        return 0