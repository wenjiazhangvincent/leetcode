class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            if d.get(x):
                del d[x]
            else:
                d[x] = '1'
        return d.keys()[0]