class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list(s)
        res = 0
        for i in range(len(s)-1,-1,-1):
            res += 26**(len(s)-1-i) * (ord(s[i]) - 64)
        return res
        