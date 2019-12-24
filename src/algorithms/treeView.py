

class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None



def printLeftView(node, levelMap, level):

    if node is None:
        return

    levelMap[level].append(node.data)
    printLeftView(node.left, levelMap, level + 1)
    printLeftView(node.right, levelMap, level + 1)




h = Node(0)
h.left = Node(1)
h.right = Node(2)
h.left.left = Node(3)
h.left.right = Node(4)

levelMap = [[], [], []]
printLeftView(h, levelMap, 0)

print(levelMap)
