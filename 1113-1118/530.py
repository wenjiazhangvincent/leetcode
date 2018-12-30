# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.tmp = set()
        
    def dfs(self, root):
        if not root:
            return
        self.tmp.add(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        if not self.tmp:
            return 0
        tmp = list(self.tmp)
        tmp.sort()
        res = 0xFFFFFFFF
        for i in range(len(tmp)-1):
            if abs(tmp[i+1] - tmp[i]) < res:
                res = abs(tmp[i+1] - tmp[i])
        return res
        