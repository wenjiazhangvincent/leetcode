class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = tmp = 0
        for x in nums:
            res, tmp = max(res, tmp+x), res
            
        return res
            