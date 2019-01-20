class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        _res = (2 * n + 0.25) ** 0.5 - 0.5
        res = int(_res)
        return res