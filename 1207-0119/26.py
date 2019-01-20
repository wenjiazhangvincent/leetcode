class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        tmp = None
        for x in nums:
            if x != tmp:
                nums[res] = x
                res += 1
                tmp = x
        return res 