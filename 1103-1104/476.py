class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 2:
            return 1^num
        b = bin(num)
        tmp = b.split('1',1)[1]
        res = ''
        for i in range(len(tmp)):
            res += str(int(tmp[i])^1)
        return int(res,2)