import Node
import UnionFindSetMeta

class UnionFindHandler:
    def __init__(self, universum = None):
        if universum is None:
            self.universum = {}
        else:
            self.universum = universum

    def make_set(self, value):
        node = Node.Node(value)
        set = UnionFindSetMeta.UnionFindSetMeta(node, node)
        node.header = set
        self.universum[value] = node

    def find(self, value):
        if value in self.universum.keys():
            return self.universum[value].header.root
        else:
            return -1

    def union(self, value_1, value_2, largest_set_is_the_root_master = True):
        if not value_1 in self.universum.keys():
            return -1
        if not value_2 in self.universum.keys():
            return -1

        set_1 = self.universum[value_1].header
        set_2 = self.universum[value_2].header

        if set_1.size >= set_2.size:
            set_large = set_1
            set_small = set_2
        else:
            set_large = set_2
            set_small = set_1

        set_large.tail.next = set_small.head

        selected_node = set_small.head
        selected_node.header = set_large
        while not selected_node.next is None:
            selected_node.next.header = set_large
            selected_node = selected_node.next
        set_large.tail = selected_node

        set_large.size = set_large.size + set_small.size
        if largest_set_is_the_root_master:
            return set_large
        else:
            set_large.root = set_small.root
            return set_large

    def everything_is_one_set(self):
        set = None
        for value in self.universum.keys():
            if (not set is None) and value.header != set:
                return False
        return True