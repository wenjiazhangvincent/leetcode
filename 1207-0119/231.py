class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        res = bin(n)[2:]
        res = res.strip('0')
        return len(res) == 1