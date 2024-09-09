class Set:
    def __init__(self, values = []):
        for value in values:
            self.insert(value)

    contains = []

    def insert(self, value):

        # if empty -- write value
        if self.contains == []:
            self.contains = [value]
            return 0

        # if inserted value is less than the first value in list -- insert it, so it becomes the first value
        if self.contains[0] > value:
            self.contains.insert(0,value)
            return 0

        # if inserted value is grater than the last value in list -- append it, so it becomes the last value
        if self.contains[-1]< value:
            self.contains.append(value)
            return 0


        # algoryhtm for binary search was snathced from Wikipedea
        l = 0
        r = len(self.contains)-1
        while True:
            if l > r:
                self.contains.insert(l, value)
                return 0
            m = int((l+r)/2)
            if self.contains[m] < value:
                l = m+1
            elif self.contains[m] > value:
                r = m-1
            else:
                return -1 # value exists

    def search(self, value):
        # if empty -- fails
        if self.contains == []:
            return -1

        # if greater than the last value -- fails
        if self.contains[0] > value:
            return -1

        # if less than the first value -- fails
        if self.contains[-1] < value:
            return -1

        l = 0
        r = len(self.contains) - 1
        while True:
            if l > r:
                self.contains.insert(l, value)
                return -1
            m = int((l + r) / 2)
            if self.contains[m] < value:
                l = m + 1
            elif self.contains[m] > value:
                r = m - 1
            else:
                return m  # value exists

    def remove(self,value):
        pos = self.search(value)

        if pos >= 0:
            self.contains.pop(value)

    def clear(self, value):
        self.contains = []


