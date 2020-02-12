class Node :

    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None


def lca(node, n1, n2) :
    if node is None :
        return

    if node.value == n1 or node.value == n2 :
        return node
    # core
    l = lca(node.left, n1, n2)
    r = lca(node.right, n1, n2)

    if l and r :
        return node

    return l if not None else r


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(lca(root, 4, 5).value)
