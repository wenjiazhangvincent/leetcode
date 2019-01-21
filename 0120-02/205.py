class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dct = {}
        for i in xrange(len(s)):
            if s[i] not in dct:
                dct[s[i]] = t[i]
            elif dct[s[i]] != t[i]:
                return False
        dct = {}
        for i in xrange(len(s)):
            if t[i] not in dct:
                dct[t[i]] = s[i]
            elif dct[t[i]] != s[i]:
                return False
        return True