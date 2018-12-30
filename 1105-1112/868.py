class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        tmp = -1
        dis = 0
        for i in range(len(s)):
            if s[i] == '1':
                if i-tmp > dis and tmp != -1:
                    dis = i - tmp
                tmp = i
        return dis
            

st = Solution()        
N = 8
print st.binaryGap(N)