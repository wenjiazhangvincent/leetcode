# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, left, right):
        if left and right:
            if left.val == right.val:
                return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
            else:
                return False
        elif not left and not right:
            return True
        else:
            return False   
                  
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)