# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return False
        tmp = [root]
        res = []
        while tmp:
            p = tmp.pop()
            if k - p.val in res:
                return True
            res.append(p.val)
            if p.left:
                tmp.append(p.left)
            if p.right:
                tmp.append(p.right)
        return False