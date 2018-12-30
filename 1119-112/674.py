class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        res = 1
        tmp = 1
        for i in xrange(len(nums)-1):
            if nums[i+1] > nums[i]:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 1
        res = max(res, tmp)
        return res