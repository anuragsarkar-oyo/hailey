

class TreeNode:
  
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
  def similar(self, nodeA, nodeB):
    x = []
    y = []
    self.dfs(nodeA, x)
    self.dfs(nodeB, y)
    if x == y:
      return True
    return False
  
  def dfs(self, node, arr):
    if node == None:
      return 
    if node.left is None and node.right is None:
      arr.append(node.val)
    self.dfs(node.right, arr)
    self.dfs(node.left, arr)
    
