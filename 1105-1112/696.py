class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if len(s) < 2:
            return 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
               res += 1
               p = i - 1
               q = i + 2
               while p >=0 and q < len(s):
                    if s[p] == s[i] and s[q] == s[i+1] and s[p] != s[q]:
                       res += 1
                       p -= 1
                       q += 1
                    else:
                        break 
        return res