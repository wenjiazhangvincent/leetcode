class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for l in grid:
            tmp = 0
            for x in l:
                tmp = x if x>tmp else tmp
            count += tmp
        
        cur = [0] * len(grid[0])
        for l in grid:
            for i in range(len(l)):
                if l[i]>cur[i]:
                    cur[i] = l[i]
        for x in cur:
            count += x
        
        for l in grid:
            for x in l:
                if x != 0:
                    count += 1
        
        return count