class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        res = [[1]]
        for i in xrange(numRows-1):
            res.append([1])
            for j in xrange(i):
                res[i+1].append(res[i][j] + res[i][j+1])
            res[i+1].append(1)
        return res
    
numRows = 2
st = Solution()
print st.generate(numRows)