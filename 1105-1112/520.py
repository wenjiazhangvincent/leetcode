class Solution(object):
    def check(self, c):
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return True
        else:
            return False
        
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        if self.check(word[0]):
            flag = self.check(word[1])
            for c in word[2:]:
                if self.check(c) != flag:
                    return False
        else:
            for c in word[1:]:
                if self.check(c) != False:
                    return False
        return True
    
word = 'USA'
st = Solution()
print st.detectCapitalUse(word)