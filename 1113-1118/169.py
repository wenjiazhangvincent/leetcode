class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = len(nums) / 2
        b = (len(nums) + 1) / 2
        for i in range(b):
            if nums[i] == nums[i+a]:
                return nums[i]