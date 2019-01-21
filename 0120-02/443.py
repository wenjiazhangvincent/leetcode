class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        tmp = ''
        count = 0
        res = 0
        for i in xrange(len(chars)):
            if i == 0 or chars[i] != chars[i-1]:
               if tmp:
                   chars[res] = tmp
                   res += 1
                   if count != 1:
                       for c in str(count):
                           chars[res] = c
                           res += 1
               tmp = chars[i]
               count = 1 
            else:
                count += 1
        if tmp:
            chars[res] = tmp
            res += 1
            if count != 1:
               for c in str(count):
                   chars[res] = c
                   res += 1
        return res
    
chars = ["a","a","a","b","b","a","a"]
st = Solution()
print st.compress(chars)