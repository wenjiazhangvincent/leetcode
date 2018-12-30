import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = int(math.ceil(area ** 0.5))
        while L <= area:
            if area%L == 0:
                return [L, area/L]
            L += 1
        