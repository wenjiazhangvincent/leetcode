class Solution(object):
    def check(self,x):
        tmp =  ord(x)
        return True if (tmp >= 65 and tmp <=90) or (tmp >= 97 and tmp <=122) else False
    
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        tmp = []
        
        for c in S:
            if self.check(c):
                tmp.append(c)
        for c in S:
            if not self.check(c):
                res.append(c)
            else:
                res.append(tmp.pop())
        return ''.join(res)