# import time
# 
# class Solution(object):
#     def check(self,s):
#         if len(s) == 1:
#             pass
#         else:
#             for i in range(len(s)-1):
#                 for j in range(i+1,len(s)):
#                     if s[i]==s[j]:
#                         return False
#         return True
#     
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0 or len(s) == 1:
#             return len(s)
#         for length in range(len(s),0,-1):
#             for j in range(len(s)-length+1):
#                 if self.check(s[j:length+j]) is True:
#                     return length         
#     
# st = Solution()
# s = "puuywsnezdufctcjqmrkiwhwerepqyehsyirqvxryrwbmbmepfpzeyvkrzajzesteakwvhnwalznmnrbu"
# print(st.lengthOfLongestSubstring(s))
# print(end-start)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = maxLen = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and usedChar[s[i]] >= start:
                start = usedChar[s[i]] + 1
            else:
                maxLen = max(maxLen,i-start+1)
                
            usedChar[s[i]] = i
        return maxLen
 
st = Solution()
s = "puuywsnezdufctcjqmrkiwhwerepqyehsyirqvxryrwbmbmepfpzeyvkrzajzesteakwvhnwalznmnrbu"
print(st.lengthOfLongestSubstring(s))
