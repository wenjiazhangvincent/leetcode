class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        elif num == 1:
            return True
        else:
            return True if (num & 0x55555554 == num) and (num & (num-1) == 0) else False