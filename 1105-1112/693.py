class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = bin(n)[2:]
        for i in range(len(tmp)-1):
            if tmp[i+1] == tmp[i]:
                return False
        return True
        