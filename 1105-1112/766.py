class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        col = len(matrix)
        row = len(matrix[0])
        res = []
        for i in range(row+col-1):
            res.append([])
        for i in range(col):
            for j in range(row):
                res[col-i+j-1].append(matrix[i][j])
        for lst in res:
            tmp = lst[0]
            for x in lst:
                if x != tmp:
                    return False
        return True