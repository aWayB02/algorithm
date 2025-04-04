class Node:

    def __init__(self, val, next=None):
        
        self.val = val
        self.next = next

dd = Node(3)
root = Node(5, next=dd)


