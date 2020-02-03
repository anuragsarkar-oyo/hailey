

class Cache:

    # b tree to maintain order
    # also keep count of hit and miss
    # time to cache

    class Node:

        def __init__(self, data):
            self.left = None
            self.right = None
            self.value = data
            self.color = "red"
            self.parent = None


    class _BST:

        def __init__(self, maxNode):
            self.maxNode = maxNode
            self.root = None

        def insert(self, value):
          newNode = Node(value)
          insertHelper(self.root, newNode)


    class _CountMap:

        def __init__(self):
            self.keepCount = {}
            self.size = maxSize

        def insert(self, node, value):
            # increment or add counter
            # also delete the element not required
            if len(self.keepCount.keys()) >= self.size:

            try:
                self.keepCount[node] += 1
            except:
                self.keepCount[node] = 1
    def __init__(self, maxSize):
        # max size of the cache [elements allowed]
        self.size = maxSize
        self.tree = self._BST(maxSize)
        self.counter = self._CountMap()


    def insert(self, value):
        # insert into cache
        nodeID = self.tree.insert(value)
        self.counter.insert(value, nodeId)
        return value

    def get(self, value):
        return self.tree.find(value)


    def clear(self, value):
        # reset cache


if __name__ == "__main__":
    print("init cache ..")
    cache = Cache(1024)
    ## test env

