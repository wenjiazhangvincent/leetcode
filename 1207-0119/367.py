class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        p, q = 0, num
        while p < q-1:
            h = (p + q) // 2
            if h ** 2 == num:
                return True
            elif h ** 2 < num:
                p = h
            else:
                q = h
        return False