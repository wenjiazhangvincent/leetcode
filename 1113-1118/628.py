class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        rnums = nums[::-1]
        tmp = rnums[0]
        nd = nums[0] * nums[1]
        rd = rnums[1] * rnums[2]
        return tmp * max(nd, rd) 
            