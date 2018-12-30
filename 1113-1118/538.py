# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lst = []
    
    def order(self, root):
        if not root:
            return 
        if root.right:
            self.order(root.right)
            
        self.lst.append(root.val)
        if self.lst:
            root.val += sum(self.lst[:-1])
        
        if root.left:
            self.order(root.left)
        
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.order(root)
        return root
        