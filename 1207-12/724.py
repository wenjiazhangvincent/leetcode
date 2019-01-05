class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        
        left, right = 0, sum(nums[1:])
        res = 0
        while left != right and res < len(nums):
            left += nums[res]
            if res < len(nums)-1:
                right -= nums[res+1]   
            else: 
                right = 0
            res += 1
        if res < len(nums):
            return res
        else:
            return -1