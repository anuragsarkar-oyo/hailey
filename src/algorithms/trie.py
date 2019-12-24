

class Node:

    def __init__(self):
        self.next = [None] * 26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return Node()

    def insert(self, value):
        # depth represents length of the tree
        depth = len(value)
        print "inserting word : " + value
        # top pointer
        head = self.root
        for level in range(depth):
            index = ord(value[level]) - ord('a')
            print "current index : " + str(index)
            # add a new node if not already available
            if not head.next[index]:
                head.next[index] = self.getNode()
            # then append to value
            head = head.next[index]
        # last element is mark word is complete .. can we
        # used for multiple elements
        head.isEndOfWord = True



    def search(self, value):
        depth = len(value)
        head = self.root
        for level in range(depth):
            index = ord(value[level]) - ord('a')
            if not head.next[index]:
                return False
            head = head.next[index]
        return head != None and head.isEndOfWord is True


    # def autoComplete(self, value):



x = Trie()
x.insert("hello")
x.insert("world")
x.insert("how")
x.insert("you")
x.search("hello")

