import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return pow(3,math.ceil(math.log(n,3))) == n if (n and n>0) else False
            