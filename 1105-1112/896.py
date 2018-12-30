class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        if length <= 1:
            return True
        tmp1 = []
        tmp2 = []
        for i in range(length-1):
            if A[i] > A[i+1]:
                tmp1.append(i)
            elif A[i] < A[i+1]:
                tmp2.append(i)
        return min(len(tmp1),len(tmp2)) == 0 