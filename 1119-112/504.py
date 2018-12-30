class Solution(object):
    def __init__(self):
        self.res = []
        
    def loop(self, num):
        if num < 7:
            self.res.append(str(num))
            return
        else:
            self.res.append(str(num % 7))
            self.loop(num / 7)
        
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 0:
            self.loop(num)
            return ''.join(self.res[::-1])
        else:
            self.loop(abs(num))
            return '-' + ''.join(self.res[::-1])
        
st = Solution()
num = -7
print st.convertToBase7(num)