class UnionFindSetMeta:
    def __init__(self, head, root = None):
        self.head = head
        self.tail = self.recalc_tail()
        if root is None:
            self.root = self.head
        else:
            self.root = root
        self.size = self.recalc_size()

    def recalc_size(self):
        if self.head is None:
            return 0
        else:
            counter = 0
            selected_node = self.head
            while not selected_node is None:
                counter+=1
                selected_node = selected_node.next
            return counter

    def recalc_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        else:
            selected_node = self.head
            while not selected_node.next is None:
                selected_node = selected_node.next
            return selected_node
