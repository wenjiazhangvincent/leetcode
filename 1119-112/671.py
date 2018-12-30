# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = set()
        
    def tra(self, root):
        if not root:
            return 
        self.res.add(root.val)
        if root.left:
            self.tra(root.left)
        if root.right:
            self.tra(root.right)
        
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tra(root)
        if len(self.res) <= 1:
            return -1
        lst = list(self.res)
        lst.sort()
        return lst[1]
        