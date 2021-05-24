import random

class Queue():
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if self.inbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
            lastV = self.outbound_stack.pop()
            while self.outbound_stack:
                self.inbound_stack.append(self.outbound_stack.pop())
            return lastV
        return self.inbound_stack

    def loopQueue(self):
        print(self.inbound_stack)

def main():
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print("Loop create queue")
    q.loopQueue()
    q.dequeue()
    q.dequeue()
    print("Loop Queue, with out the 2 first elements")
    q.loopQueue()

if __name__ == '__main__':
    main()