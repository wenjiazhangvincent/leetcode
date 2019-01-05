row = [1]
for i in xrange(10):
    row = [x + y for x, y in zip([0]+row, row+[0])]
    print row