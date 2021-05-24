from node import Node
import random

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        data = "The stack is empty"
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
        return data

    def peek(self):
        if self.top:
            return self.top.data
        return "The stack is empty"

    def clear(self):
        while self.top:
            self.pop()

    def __contains__(self, data):
        if self.top:
            p = self.top
            while p:
                if p.data == data:
                    return True
                p = p.next
        return False

    def __loop__(self):
        print("loop stack")
        if self.top:
            p = self.top
            while p:
                print(p.data)
                p = p.next
        else:
            return "Stack is Empty"

    def __iter__(self):
        if self.top:
            p = self.top
            while p:
                v = p.data
                p = p.next
                yield v
        else:
            return "Stack is Empty"


def main():
    food = Stack()
    food.push("egg")
    food.push("ham")
    food.push("spam")
    print("-- iterator --")
    myIter = food.__iter__()
    print(next(myIter))
    print(next(myIter))
    print("\n-- pop --")
    print(food.pop())
    food.__loop__()
    print(food.peek())
    print("\n-- clear stack --")
    food.clear()
    print(food.peek())
    food.__loop__()

if __name__ == '__main__':
    main()