# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
        self.count = []
        
    def check(self,root,i):
        if not root:
            return
        if i >= len(self.res):
            self.res.append(root.val)
            self.count.append(1)
        else:
            self.res[i] += root.val
            self.count[i] += 1
        if root.left:
            self.check(root.left,i+1)
        if root.right:
            self.check(root.right,i+1)
        
        
        
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.check(root, 0)
        for i in range(len(self.res)):
            self.res[i] = float(self.res[i]) / self.count[i]
        return self.res 
        