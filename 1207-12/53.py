class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        prev_max_sum = nums[0]
        for i in range(1, len(nums)):
            prev_max_sum = nums[i] + max(prev_max_sum, 0)
            max_sum = max(max_sum, prev_max_sum)
        return max_sum