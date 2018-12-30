# class Solution(object):
#     def longestWord(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         if not words:
#             return ""
#         
#         tmp = []
#         for word in words:
#             _set = set(list(word))
#             tmp.append(len(_set))
#         _max = max(tmp)
#         
#         res = [] 
#         for i in xrange(len(tmp)):
#             if tmp[i] == _max:
#                 res.append(words[i])
#         
#         if len(res) == 1:
#             return res[0]
#         
#         _res = res[0]
#         for word in res[1:]:
#             if word < _res:
#                 _res = word
#         return _res

# class Solution(object):
#     def longestWord(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         if not words:
#             return ""
#         
#         words.sort(key = lambda x:len(x), reverse = True)
#         length = len(words)
#         res = [0] * length
#         visited = []
#         for i in xrange(length):
#             for j in xrange(len(visited)):
#                 if words[i] in visited[j]:
#                     res[j] += 1
#             visited.append(words[i])
#         
#         print visited
#         print res
#         
#         tmp = max(res)
#         cnd = []
#         for i in xrange(length):
#             if res[i] == tmp:
#                 cnd.append(visited[i])
#         return cnd[-1]
                

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        
        count = []
        for word in words:
            tmp = 0
            for i in xrange(len(word)-1):
                if word[:i+1] in words:
                    tmp += 1
                else


    
st = Solution()
# words = ["w","wo","wor","worl", "world"]
words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
print st.longestWord(words)
                    
        
            










