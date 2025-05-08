class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Tree(5)
root.left = Tree(3)
root.right = Tree(4)
root.left.left = Tree(2)
root.left.right = Tree(8)
root.right.left = Tree(6)
root.right.right = Tree(7)


def max_tree(node: Tree) -> int:
    if node is None:
        return float('-inf')
    return max(node.value, max_tree(node.left), max_tree(node.right))


print(max_tree(root))