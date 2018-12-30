class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
#         x = min(lambda i:ops[i][0] for i in xrange(len(ops)))
#         y = min(lambda i:ops[i][1] for i in xrange(len(ops)))
        if not ops:
            return m * n
        x = y =0xFFFFFFFF
        for op in ops:
            x = min(x, op[0])
            y = min(y, op[1])
        return x * y

m = 3
n = 4
ops = [[2,2]]
x = map(min, ops[i][0] for i in xrange(len(ops)))
print x