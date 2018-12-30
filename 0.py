grid = [ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

for j in xrange(4):
    print max(grid[j]), max(grid[:][j])