# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = {}
        
    def dfs(self, root):
        if not root:
            return 
        self.res[root.val] = self.res[root.val] + 1 if root.val in self.res else 1
        self.dfs(root.left)
        self.dfs(root.right)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dfs(root)
        _max = max(x for i,x in self.res.iteritems())
        lst = [i for i in self.res if self.res[i] == _max]
        return lst