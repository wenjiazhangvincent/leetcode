import collections

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cnt = collections.Counter(nums)
        times = max(cnt.values())
        if times == 1:
            return 1
        
        res = 0
        rnums = nums[::-1]
        for k, v in cnt.items():
            if v == times:
                res = max(res,
                          nums.index(k) + rnums.index(k) 
                           )
        return len(nums) - res