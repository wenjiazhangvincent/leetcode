class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        p = q = 0
        res = 0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                g.pop(p)
                s.pop(q)
                res += 1
            else:
                q += 1
        return res