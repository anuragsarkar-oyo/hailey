
class Tree:
  
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not (preorder and inorder):
            return None
        x = preorder[0]
        root = Tree(x)
        l = inorder.index(x)
        root.left = self.buildTree(preorder[1:l+1], inorder[:l])
        root.right =  self.buildTree(preorder[l+1:], inorder[l+1:])
        return root
  

inOrder =[4, 2, 5, 1, 3, 6]
preOrder = [1, 2, 4, 5, 3, 6]

root = Solution().buildTree(preOrder, inOrder)
print(root)