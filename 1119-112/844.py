class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        r1 = []
        r2 = []
        for c in S:
            if c != '#':
                r1.append(c)
            else:
                if r1:
                    r1.pop(len(r1)-1)
        for c in T:
            if c != '#':
                r2.append(c)
            else:
                if r2:
                    r2.pop(len(r2)-1)
        return r1 == r2