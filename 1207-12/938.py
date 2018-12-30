# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
    
    def dfs(self, root, L, R):
        if not root:
            return
        if L <= root.val <= R:
            self.res += root.val
        self.dfs(root.left, L, R)
        self.dfs(root.right, L, R)
        
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, L, R)
        return self.res 