import random
class ListQueue():
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        for i in self.items:
            print(i)

def main():
    q = ListQueue()
    q.enqueue("asd")
    q.enqueue("sdf")
    q.enqueue("dfg")
    print("First traverse")
    q.traverse()
    print("\ndequeue: ", q.dequeue())
    print("\nSecond Traverse")
    q.traverse()

if __name__ == '__main__':
    main()