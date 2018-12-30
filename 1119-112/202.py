class Solution(object):
    def __init__(self):
        self.check = []
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n in self.check:
            return False
        self.check.append(n)
        tmp = 0
        while n >= 10:
            tmp += (n % 10) ** 2
            n /= 10
        tmp += n ** 2
        return self.isHappy(tmp)
            
