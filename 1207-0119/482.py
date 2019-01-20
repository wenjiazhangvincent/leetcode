class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tmp = [c.upper() for c in S if c != '-']
        tms = len(tmp) // K
        rst = len(tmp) % K
        if rst > 0:
            res = [''.join(tmp[:rst])]
        else:
            res = []
        for i in xrange(tms):
            res.append(''.join(tmp[rst + K*i:rst + K + K*i]))
        res = '-'.join(res)
        return res