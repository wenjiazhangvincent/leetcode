class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1,N+1):
            s = str(i)
            if '3' not in s and '4' not in s and '7' not in s and ('2' in s or '5' in s or '6' in s or '9' in s):
                res += 1
        return res