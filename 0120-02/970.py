import math

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound < 1:
            return []
        if x != 1:
            x_max = int(math.log(bound) / math.log(x))
            x_cdd = [x ** i for i in xrange(x_max+1)]
        else:
            x_cdd = [1]
        if y != 1:
            y_max = int(math.log(bound) / math.log(y))
            y_cdd = [y ** i for i in xrange(y_max+1)]
        else:
            y_cdd = [1]
        res = set()
        for a in x_cdd:
            for b in y_cdd:
                if a + b <= bound:
                    res.add(a+b)
                else:
                    break
        res = list(res)
        return res
        
x = 1
y = 2
bound = 100
st = Solution()
print st.powerfulIntegers(x, y, bound)