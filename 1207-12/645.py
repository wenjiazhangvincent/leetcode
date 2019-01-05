import collections

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dup = collections.Counter(nums).most_common(1)[0][0]
        mis = list(set(i for i in xrange(1, n+1)) - set(nums))[0] 
        return [dup, mis]