class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = []
        while x != 0:
            tmp.append(x % 10)
            x = x // 10
        if tmp[::-1] == tmp:
            return True
        else:
            return False
            