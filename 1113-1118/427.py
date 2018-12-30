"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def DFS(grid):
            if not grid:
                return 
            isLeaf = all(grid[0][0]==x for x in itertools.chain(*grid))
            if isLeaf:
                return Node(grid[0][0]==1,True,None,None,None,None)
#             col, row = len(grid), len(grid[0])
            l, w = len(grid), len(grid[0])
            return Node(
                False,
                False,
                DFS([[grid[i][j] for j in range(w//2)] for i in range(l//2)]),
                DFS([[grid[i][j] for j in range(w//2, w)] for i in range(l//2)]),
                DFS([[grid[i][j] for j in range(w//2)] for i in range(l//2, l)]),
                DFS([[grid[i][j] for j in range(w//2, w)] for i in range(l//2, l)]),
#                 DFS(grid[:col//2][:row//2]),
#                 DFS(grid[:col//2][row//2:]),
#                 DFS(grid[col//2:][:row//2]),
#                 DFS(grid[col//2:][row//2:])
                )
            
        return DFS(grid)