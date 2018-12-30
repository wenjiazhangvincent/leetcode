class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B:
            return True
        if len(A) != len(B):
            return False
        A = list(A)
        B = list(B)
        for i in range(len(A)):
            A.append(A.pop(0))
            if A == B:
                return True
        return False