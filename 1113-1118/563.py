# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
        
    def tra(self, root):
        if not root:
            return
        tmp = 0
        if root.left:
            self.tra(root.left)
            tmp += root.left.val
            root.val += root.left.val 
        if root.right:
            self.tra(root.right)
            tmp -= root.right.val
            root.val += root.right.val
        self.res += abs(tmp)
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.tra(root)
        return self.res