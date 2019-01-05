class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        res = 0
        for c in s: 
            if c == '1':
                res += 1 
        return res