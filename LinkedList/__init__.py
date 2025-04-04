"""
04.04.2024
DSA g1
"""


class Node:

    def __init__(self, val, next=None):

        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None  # начало списка

    def append(self, val):
        "add item to end"
        new_node = Node(val)

        if self.head is None:

            self.head = new_node
            return

        current: Node = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, val):

        new_node = Node(val, self.head)
        self.head = new_node

    def display(self):

        current: Node = self.head

        while current.next:

            print(current.val, end=" ")

            current = current.next

        print(current.val)


root = LinkedList()
root.append(1)
root.append(2)
root.append(3)
root.display()
root.prepend(5)
root.display()
root.prepend(6)
root.display()
