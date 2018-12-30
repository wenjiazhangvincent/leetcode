# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
        
    def tra(self, root, flag):
        if not root:
            return 
        if not root.left and not root.right and flag:
            self.res += root.val
        self.tra(root.left, True)
        self.tra(root.right, False)
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.tra(root, False)
        return self.res