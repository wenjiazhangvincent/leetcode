class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 1:
            return False
        
        tmp = [i for i in xrange(2, length//2+1) if length % i == 0]
        tmp.append(1)
        for i in tmp:
            std = s[:i] 
            j = 2 * i
            while j <= length:
                if s[j-i:j] != std:
                    break
                j += i
            if j > length:
                return True
        return False
    
s = "zzz"
st = Solution()
print st.repeatedSubstringPattern(s)