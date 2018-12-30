# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check(self,node):
        if not node:
            return None
        while node:
            if node.val > self.R:
                node = node.left
            elif node.val < self.L:
                node = node.right
            else:
                return node
            
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        self.L = L
        self.R = R 
        
        tmp = self.check(root)
        if not tmp:
            return 
        res = [tmp]
        
        while res:
            node = res.pop()
            node.left = self.check(node.left)
            node.right = self.check(node.right)
            res.extend(filter(None,[node.left,node.right]))
            
        return tmp
