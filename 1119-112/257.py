# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
        
    def tra(self, root, pre):
        if not root:
            return 
        tmp = pre + '->' + str(root.val)
        if not root.left and not root.right:
            self.res.append(tmp)
        else:
            if root.left:
                self.tra(root.left, tmp)
            if root.right:
                self.tra(root.right, tmp)
        
        
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.tra(root, '')
        return [item[2:] for item in self.res]