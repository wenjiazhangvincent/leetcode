import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lst = []
        tmp = ''
        i = 0
        while i < len(paragraph):
            while i < len(paragraph) and paragraph[i].isalpha():
                tmp += paragraph[i].lower()
                i += 1
            if tmp:
                lst.append(tmp)
            tmp = ''
            i += 1
        
        for i in xrange(len(lst)-1, -1, -1):
            if lst[i] in banned:
                lst.pop(i)
        
        dct = collections.Counter(lst)
        print dct
        return dct.most_common(1)[0][0]
        
        
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
st = Solution()
print st.mostCommonWord(paragraph, banned)