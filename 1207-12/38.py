class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in xrange(1, n):
            tmp = ''
            cc = ''
            count = 0
            for c in res:
                if c != cc:
                    if cc != '':
                        tmp += '%s%s' % (count, cc)
                    cc = c
                    count = 1
                else:
                    count += 1
            if res[-1] == cc:
                tmp += '%s%s' % (count, cc)
            res = tmp
        return res