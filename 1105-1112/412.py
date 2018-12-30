class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(0,n,1):
            res.append(str(i+1))
        if n >= 3:
            for i in range(2,n,3):
                res[i] = 'Fizz'
        if n >= 5:
            for i in range(4,n,5):
                res[i] = 'Buzz'
        if n >= 15:
            for i in range(14,n,15):
                res[i] = 'FizzBuzz'
        return res