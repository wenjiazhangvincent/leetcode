# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = True
        
    def dfs(self, root):
        if not root:
            return 0 
        ld = self.dfs(root.left)
        rd = self.dfs(root.right)
        if abs(ld-rd) > 1:
            self.res = False
        return max(ld, rd) + 1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.dfs(root)
        return self.res