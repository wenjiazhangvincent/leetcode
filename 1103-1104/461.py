class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        Z = bin(z)
        count = 0
        for i in Z:
            if i == '1':
                count += 1
        return count