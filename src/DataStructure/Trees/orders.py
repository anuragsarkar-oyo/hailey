

class Tree:

  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

  def postOrder(self, node):
    if not node:
      return
    self.postOrder(node.left)
    self.postOrder(node.right)
    print(node.val)

  def levelOrder(self, node):
    q = []
    if not node:
      return
    q.append(node)
    q.append(None)
    while len(q) > 1:
      x = q.pop(0)
      if x is None:
        q.append(None)
      else:
        if x.left is not None:
          q.append(x.left)
        if x.right is not None:
          q.append(x.right)
        print(x.val)

  def inOrder(self, node):
    if not node:
      return
    self.inOrder(node.left)
    print(node.val)
    self.inOrder(node.right)

  def inOrderWithoutRecurssion(self, node):
    x = node
    stack = []
    while True:
      if x is not None:
        stack.append(x)
        x = x.left
      elif stack:
        x = stack.pop()
        print(x.val)
        x = x.right
      else:
        break

  def preOrder(self, node):
    if not node:
      return
    print(node.val)
    self.preOrder(node.left)
    self.preOrder(node.right)

  def height(self, node):
    if not node:
      return 0
    return 1 + max(self.height(node.left), self.height(node.right))
  
  def unique(self, n):
    z = []
    
  
  def isValidBST(self, root):
        import sys
        
        def helper(node,lowbond, upbond):
            if not node: return True
            if lowbond < node.val and node.val < upbond:
                left = helper(node.left, lowbond, node.val)
                right = helper(node.right, node.val, upbond)
            else:
                return False
            return left and right
        return helper(root,100000 * -1, 100000)

h = Tree(1)
h1 = Tree(2)
h2 = Tree(3)
h3 = Tree(4)
h4 = Tree(5)
h.left = h1
h.right = h2
h2.left = h3
h2.right = h4

# h.postOrder(h)
# print("----")
# h.inOrder(h)
# print("----")
print(h.height(h))
# print("----")
# h.preOrder(h)
