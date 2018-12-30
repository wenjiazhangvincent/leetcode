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
            return 0
        ld, rd = self.tra(root.left), self.tra(root.right)
        self.res = max(self.res, ld+rd)
        return max(ld,rd) + 1
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tra(root)
        return self.res
        