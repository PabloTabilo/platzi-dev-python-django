import random

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        self.capacity = capacity
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __fill__(self):
        for i in range(self.capacity):
            self.items[i] = random.randint(1,100)

    def __sum__(self):
        tot = 0
        for i in range(self.capacity):
            tot += self.items[i] if self.items[i] is not None else 0
        return tot