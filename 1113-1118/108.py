# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def divide(left, right):
            if left > right:
                return None
            mid = (left + right) / 2
            tmp = TreeNode(nums[mid])
            tmp.left = divide(left, mid-1)
            tmp.right = divide(mid+1, right) 
            return tmp
            
        left, right = 0, len(nums)-1
        return divide(left, right)