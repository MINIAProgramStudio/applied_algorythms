class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_element = next_node
    value: None
    pointer: None

class SortedLinkedListSet:
    def __init__(self, first_node = None):
        self.first_node = first_node

    first_node: None

    def search(self, value):
        selected_node = self.first_node
        counter = 0

        # search loop
        while True:
            # if no next node -- search failed
            if selected_node is None:
                return -1
            else:
                # if value is found -- return position of the value
                if selected_node.value == value:
                    return counter

                # if value is not found but next node exists -- continue
                else:
                    selected_node = selected_node.next_node
                    counter += 1

    def length(self):
        selected_node = self.first_node
        counter = 1

        # counter loop
        while True:
            if selected_node is None:
                return counter
            else:
                selected_node = selected_node.next_node
                counter += 1

    def add(self, value):
        if self.search(value) == -1:
            new_node = Node(value,self.first_node)
            self.first_node = new_node

    def remove(self, value):


        selected_node = self.first_node


        # search loop
        while True:
            # if no next node -- search failed
            if selected_node is None:
                return -1
            else:
                # if value is found -- delete it and join nearby nodes
                if selected_node.value == value:


                # if value is not found but next node exists -- continue
                else:
                    selected_node = selected_node.next_node
