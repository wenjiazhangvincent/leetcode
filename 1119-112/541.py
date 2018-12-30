class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        first = length / (2 * k)
        last = length % (2 * k)
        res = ""
        for i in xrange(first):
            res = res + s[2*k*i:2*k*i+k][::-1] + s[2*k*i+k:2*k*i+2*k]
        if last < k:
            res = res + s[2*k*first:length][::-1] 
        else:
            res = res + s[2*k*first:2*k*first+k][::-1] + s[2*k*first+k:length]
        return res