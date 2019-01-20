class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n // 5 + self.trailingZeroes(n // 5) if n // 5 != 0 else 0 