class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        vis = []
        dup = set()
        for c in s:
            if c not in vis:
                vis.append(c)
            else:
                dup.add(c)
        if set(vis) == dup:
            return -1
        x = ''
        for c in vis:
            if c not in dup:
                x = c
                break
        for i in xrange(len(s)):
            if s[i] == c:
                return i