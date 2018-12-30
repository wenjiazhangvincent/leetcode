class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = set(i+1 for i in range(len(nums)))
        b = set(nums)
        return list(a - b)