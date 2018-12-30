class Solution(object):
    def __init__(self):
        self.t = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s) - 1:
            if self.t[s[i]] < self.t[s[i+1]]:
               res += self.t[s[i+1]] - self.t[s[i]]
               i += 2
            else:
                res += self.t[s[i]]
                i += 1
        if i < len(s):
            res += self.t[s[i]]
        return res
                                       