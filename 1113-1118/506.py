class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        length = len(nums)
        res = [""] * length 
        tmp = sorted(nums, reverse=True)
        if length == 1:
            return ["Gold Medal"]
        if length >= 2:
            res[nums.index(tmp[0])] = "Gold Medal"
            res[nums.index(tmp[1])] = "Silver Medal"
            if length >= 3:
                res[nums.index(tmp[2])] = "Bronze Medal"
        if length <= 3:
            return res
        for i in xrange(length-3):
            res[nums.index(tmp[i+3])] = str(i+4)
        return res