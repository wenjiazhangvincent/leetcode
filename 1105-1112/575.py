class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        a = len(set(candies))
        b = len(candies) / 2
        return b if a>b else a