class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self):
        return str(self.data)