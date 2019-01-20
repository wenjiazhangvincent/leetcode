class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        tmp = s.split(' ')
        res = 0
        for x in tmp:
            if x:
                res += 1
        return res
    
s = "Of all the gin joints in all the towns in all the world,   "
st = Solution()
print st.countSegments(s)