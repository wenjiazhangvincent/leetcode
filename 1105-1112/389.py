class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return t[0]
        a = list(s)
        a.sort()
        b = list(t)
        b.sort()
        for i in range(len(a)):
            if a[i] != b[i]:
                return b[i]
        return b[-1]