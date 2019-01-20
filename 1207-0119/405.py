class Solution(object):
    def toHex(self, num):
        return ''.join('0123456789abcdef'[(num >> 4 * i) & 15]
                       for i in xrange(8)
                       )[::-1].lstrip('0') or '0'