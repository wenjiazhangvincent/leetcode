# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = True
        self.tmp = 0
        
    def dfs(self, root):
        if not root:
            return
        if root.val != self.tmp:
            self.res = False
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
        
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.tmp = root.val
        self.dfs(root)
        return self.res
        