class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split(' ')
        for i in range(len(tmp)):
            tmp[i] = tmp[i][::-1]
        s = ' '.join(tmp)
        return s