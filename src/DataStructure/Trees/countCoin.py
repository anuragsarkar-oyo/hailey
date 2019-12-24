

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count(node, x):
    if node is None:
        return 0
    l, r = count(node.left, x) , count(node.right, x)
    x.append(abs(l) + abs(r))
    return node.val + l + r - 1


h = Node(3)
h.left = Node(0)
h.right = Node(0)
x = []
print(count(h, x))
print(x)
