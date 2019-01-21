from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        res = []
        pC = Counter(p)
        sC = Counter(s[:len(p)-1])
        for i in xrange(len(p)-1, len(s)):
            sC[s[i]] += 1
            if sC == pC:
                res.append(i-len(p)+1)
            sC[s[i-len(p)+1]] -= 1
            if sC[s[i-len(p)+1]] == 0:
                del sC[s[i-len(p)+1]]
        return res
            