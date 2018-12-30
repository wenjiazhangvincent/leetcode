import collections

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = collections.Counter(s)
        if tmp['A'] > 1 or 'LLL' in s:
            return False
        return True