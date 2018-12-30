"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.res = []
        
    def check(self, root, i):
        if not root:
            return 
        if i >= len(self.res):
            self.res.append([root.val])
        else:
            self.res[i].append(root.val)
        if root.children:
            for chi in root.children:
                self.check(chi, i+1)
        
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self.check(root, 0)
        return self.res