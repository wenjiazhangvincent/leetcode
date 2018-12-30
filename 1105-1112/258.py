class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = str(num)
        sum = 0
        while len(tmp) > 1:
            for x in tmp:
                sum += int(x)
            tmp = str(sum)
            sum = 0
        return int(tmp)