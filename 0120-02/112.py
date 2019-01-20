# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = False
    
    def dfs(self, root, tmp):
        if not root:
            return
        tmp += root.val
        if tmp == self.std and (not root.left) and (not root.right):
            self.res = True
        self.dfs(root.left, tmp)
        self.dfs(root.right, tmp)
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        self.std = sum
        self.dfs(root, 0)
        return self.res
        