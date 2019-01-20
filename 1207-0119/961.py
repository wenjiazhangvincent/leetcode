class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in xrange(1, len(A)):
            if A[i] == A[i-1]:
                return A[i]
            