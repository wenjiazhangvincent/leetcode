class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        result = A[len(A)-1] - A[0] - 2 * K
        if result >= 0:
            return result
        else:
            return 0