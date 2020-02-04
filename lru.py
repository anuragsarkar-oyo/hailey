class Node :

    def __init__(self, value) :
        self.left = None
        self.right = None
        self.data = value


# global
m = {}  # which will point my data ...
size = 3  # cache size
startingPoint = None


def fetch(value) :
    if m[value] is None :
        startingPoint = Node(value)
        # code to be added here ??
    else :
        return m[value]
