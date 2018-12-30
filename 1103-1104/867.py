class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A[0])
        col = len(A)
        B = []
        for i in range(row):
            tmp = []
            for j in range(col):
                tmp.append(A[j][i])
            B.append(tmp)
        return B