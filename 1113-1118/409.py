class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        dict = {}
        res = 0
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for v in dict.values():
            res += v / 2 * 2
        
        flag = False
        for v in dict.values():
            if v % 2 == 1:
                flag = True
                break
        return res + flag