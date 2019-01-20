class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in xrange(length):
            if digits[-1-i] == 9:
                digits[-1-i] = 0
            else:
                digits[-1-i] += 1
                break
        if digits[0] == 0:
            digits = [1] + digits
        return digits