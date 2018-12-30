# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lst = []
        
    def haha(self, root):
        
        if not root:
            return 
        
        if root.left:
            self.haha(root.left)
        self.lst.append(root.val)
        if root.right:
            self.haha(root.right)
            
        
     
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """   
        
        self.haha(root)
        res = TreeNode(self.lst[0])
        pre = res
        for i in range(len(self.lst)-1):
            tmp = TreeNode(self.lst[i+1])
            pre.right = tmp
            pre = tmp
            
        return res
            