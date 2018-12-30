# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
        
    def traverse(self, t):
        if not t:
            return
        self.res.append(str(t.val))
        if t.left:
            self.res.append('(')
            self.traverse(t.left)
            self.res.append(')')
        if t.right and t.left:
            self.res.append('(')
            self.traverse(t.right)
            self.res.append(')')
        elif t.right and not t.left:
            self.res.extend(['(',')','('])
            self.traverse(t.right)
            self.res.append(')')
            
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.traverse(t)
        return ''.join(self.res)
        