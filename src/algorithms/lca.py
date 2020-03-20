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


def preorder(node) :
    if node is None :
        return
    print(node.value)  # process
    preorder(node.left)
    preorder(node.right)


def inorder(node) :
    if node is None :
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)


def postOrder(node) :
    if node is None :
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.value)

m = {} # [level, []]
def levelOrder(node, m, level):
    if node is None:
        return
    try:
        m[level].append(node.value)
    except:
        m[level] = [node.value]
    levelOrder(node.left, m, level+1)
    levelOrder(node.right, m, level + 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

levelOrder(root, m, 0)
print(m)