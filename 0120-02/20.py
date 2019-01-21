class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        tmp = []
        dct = {
            '(': ')',
            '{': '}',
            '[': ']',
            }
        for c in s:
            if c in dct:
                tmp.append(dct[c])
            elif not tmp or tmp[-1] != c:
                return False
            else:
                tmp.pop(-1)
        if not tmp:
            return True
        else:
            return False