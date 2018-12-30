class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        else:
            a = 2
            b = 3
            t = n - 3
            for i in xrange(t):
                tmp = b
                b += a 
                a = tmp
            return b
        
        
    
                