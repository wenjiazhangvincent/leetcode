class Solution(object):
    def check(self,x):
        y = x
        tmp = []
        while x != 0:
            tmp.append(x%10)
            x = x / 10
        if 0 in tmp:
            return False
        for i in range(len(tmp)):
            if y%tmp[i] != 0:
                return False
        return True
            
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for x in range(left,right+1):
            if self.check(x) is True:
                result.append(x)
        return result