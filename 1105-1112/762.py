class Solution(object):
    def isPrime(self, n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n%2 == 0 or n%3 == 0:
            return False
        return True
    
    def count(self, n):
        tmp = bin(n)[2:]
        c = 0
        for x in tmp:
            if x == '1':
                c += 1
        return c
    
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for i in range(L,R+1):
            if self.isPrime(self.count(i)):
                res += 1
        return res