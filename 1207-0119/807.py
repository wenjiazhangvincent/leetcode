class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        row_list = [max(grid[i]) for i in xrange(row)]
        col_list = [0 for i in xrange(col)]
        for i in xrange(col):
            col_list[i] = max(grid[j][i] for j in xrange(row)) 
        gridNew = [[min(row_list[i], col_list[j]) for i in xrange(row)] for j in xrange(col)]
        gridNew = zip(*gridNew)
        res = sum(gridNew[i][j] - grid[i][j] for i in xrange(row) for j in xrange(col))
        return res
                
                
grid = [ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

st = Solution()
print st.maxIncreaseKeepingSkyline(grid)