class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(M), len(M[0])
        res = [[0 for j in xrange(col)] for i in xrange(row)] 
        for i in xrange(row):
            for j in xrange(col):
                tmp = [M[i][j]]
                if i > 0:
                    tmp.append(M[i-1][j])
                if i < row-1:
                    tmp.append(M[i+1][j])
                if j > 0:
                    tmp.append(M[i][j-1])
                if j < col-1:
                    tmp.append(M[i][j+1]) 
                if i > 0 and j > 0:
                    tmp.append(M[i-1][j-1])
                if i > 0 and j < col-1:
                    tmp.append(M[i-1][j+1])
                if i < row-1 and j > 0:
                    tmp.append(M[i+1][j-1])
                if i < row-1 and j < col-1:
                    tmp.append(M[i+1][j+1])
                res[i][j] = sum(tmp) / len(tmp)
        return res