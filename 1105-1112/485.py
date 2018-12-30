class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        res = 0
        for x in nums:
            if x == 1:
                tmp += 1
            else:
                res = max(res,tmp)
                tmp = 0
        return max(res,tmp)
            