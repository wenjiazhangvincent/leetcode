class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        count = 0
        diff = 0
        for i in range(row):
            for j in range(col):
                count += grid[i][j]
                diff += grid[i][j] - 1 if grid[i][j] else 0
                if j != 0:
                    diff += min(grid[i][j-1],grid[i][j])
        for j in range(col):
            for i in range(row):
                if i != 0:
                    diff += min(grid[i-1][j],grid[i][j])
        return count * 6 - diff * 2