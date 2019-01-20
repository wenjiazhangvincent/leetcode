class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        tmp = nums[:]
        tmp.sort()
        if tmp[-1] >= 2 * tmp[-2]:
            return nums.index(tmp[-1])
        return -1