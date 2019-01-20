class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        _sum = sum(nums[:k])
        _max = _sum
        for i in xrange(k, length):
            _sum -= nums[i-k]
            _sum += nums[i]
            if _sum > _max:
                _max = _sum
        _avg = _max / float(k)
        return _avg