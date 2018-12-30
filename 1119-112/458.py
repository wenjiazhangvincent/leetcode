import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        x = minutesToTest // minutesToDie + 1
        if buckets <= x:
            return 1
        tmp = math.log(buckets, x)
        return int(math.ceil(tmp))
    

st = Solution()
print st.poorPigs(1,1,1)
# print st.poorPigs(1000,15,60)