# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def haha(self,root,res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
        self.haha(root.left, res)
        self.haha(root.right, res)
        return res
            
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        s1 = self.haha(root1, [])
        s2 = self.haha(root2, [])
        return s1==s2
        