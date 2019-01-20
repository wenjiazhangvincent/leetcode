class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        if len(num1) < len(num2):
            tmp = num1 
            num1 = num2
            num2 = tmp
            
        num1 = list(num1)
        num1.reverse()
        num2 = list(num2)
        num2.reverse()
             
        flag = False
        for i in xrange(len(num2)):
            tmp = (ord(num1[i])-ord('0')) + (ord(num2[i])-ord('0')) + flag
            if tmp > 9:
                flag = True
                tmp %= 10
            else:
                flag = False 
            res += str(tmp)
         
        for i in xrange(len(num2), len(num1)):
            tmp = (ord(num1[i])-ord('0')) + flag
            if tmp > 9:
                flag = True
                tmp %= 10
            else:
                flag = False 
            res += str(tmp)
        
        if flag:
            res += '1'
             
        res = res[::-1]
        return res

num1 = '98'
num2 = '9'
st = Solution()
print st.addStrings(num1, num2)