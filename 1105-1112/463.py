class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid)
        row = len(grid[0])
        
        count = 0
        for i in range(col):
            for j in range(row):
                if grid[i][j] == 0:
                    continue
                
                if i == 0:
                    count += 1
                elif grid[i-1][j] == 0:
                    count += 1
                    
                if i == col-1:
                    count += 1
                elif grid[i+1][j] == 0:
                    count += 1
                    
                if j == 0:
                    count += 1
                elif grid[i][j-1] == 0:
                    count += 1
                    
                if j == row-1:
                    count += 1
                elif grid[i][j+1] == 0:
                    count += 1
        return count