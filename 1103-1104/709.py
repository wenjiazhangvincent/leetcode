class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        for i in range(len(str)):
            if str[i]>='A' and str[i]<='Z':
                str = str[0:i] + chr(ord(str[i])+32) + str[i+1:len(str)]
        return str
    