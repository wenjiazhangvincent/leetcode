class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        _min, res = float('inf'), 0
        for x in prices:
            _min, res = min(_min, x), max(res, x-_min) 
        return res