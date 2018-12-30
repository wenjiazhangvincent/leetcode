class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lst = [c.lower() for c in licensePlate if c.isalpha()]
        tmp = set(lst)
        words.sort(key = lambda x:len(x))
        print words
        for word in words:
            if all(lst.count(c) <= word.count(c) for c in tmp):
                return word
            
        
        
        
st = Solution()
licensePlate = "1s3 PSt"
words = [ "steps", "stripe","step", "stepple"]
print st.shortestCompletingWord(licensePlate, words)