# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        n = (left + right) / 2
        res = guess(n)
        while res != 0:
            if res == 1:
                left = n + 1
            else:
                right = n - 1
            n = (left + right) / 2
            res = guess(n)
        return n