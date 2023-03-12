

class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node(data={self.data})"

class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, data) -> None:
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def __repr__(self):
        return f"Stack(top={self.top})"
