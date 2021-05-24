import random
from array import Array

class Grid():
    def __init__(self, rows, colums, fill_value=None):
        self.data = Array(rows)
        for i in range(rows):
            self.data[i] = Array(colums, fill_value=None)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __fill__(self):
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                self.data[r][c] = random.randint(1,100)
        print(self.__str__())

    def __str__(self):
        res = ""
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                res += str(self.data[r][c]) + " "
            res += '\n'
        return str(res)