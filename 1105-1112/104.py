# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max = 1
        
    def check(self,root,d):
        if not root:
            return 0
        self.max = max(self.max,d)
        
        if root.left:
            self.check(root.left,d+1) 
        if root.right:
            self.check(root.right,d+1)
        return self.max
           
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.check(root,1) 