import random
from double_linked_list import TwoWayNode

class Queue():
    def __init__(self):
        self.head, self.tail = None, None
        self.count = 0

    def enqueue(self, data):
        node = TwoWayNode(data, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        c = self.head
        if self.count == 1:
            self.count -= 1
            self.tail = None
            self.head = None
        elif self.count > 1:
            self.count -= 1
            self.head = self.head.next
            self.head.previous = None
        return c.data

    def __str__(self):
        res = "empty"
        if self.head:
            res = ""
            p = self.head
            while p != None:
                res += p.data + " --> "
                p = p.next
            res = res[:-5]
        return res



def main():
    food = Queue()
    food.enqueue("eggs")
    food.enqueue("ham")
    food.enqueue("spam")
    print(food.head.data)
    print(food.head.next.data)
    print(food.tail.data)
    print(food.tail.previous.data)
    print(food.count)
    print(food.dequeue())
    print(food.head.data)

if __name__ == '__main__':
    main()