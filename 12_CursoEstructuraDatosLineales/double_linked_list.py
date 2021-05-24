from node import Node

class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data, next)
        self.previous = previous