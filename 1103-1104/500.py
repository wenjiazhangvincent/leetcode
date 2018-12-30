class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = [
            ['Q','W','E','R','T','Y','U','I','O','P',
              'q','w','e','r','t','y','u','i','o','p'],
            ['A','S','D','F','G','H','J','K','L',
             'a','s','d','f','g','h','j','k','l'],
            ['Z','X','C','V','B','N','M',
             'z','x','c','v','b','n','m']
            ]
        
        res = []
        for s in words:
            if s[0] in d[0]:
                t = 0
            elif s[0] in d[1]:
                t = 1
            else:
                t = 2
            flag = True
                
            for c in s[1:]:
                if c in d[0]:
                    x = 0
                elif c in d[1]:
                    x = 1
                else:
                    x = 2
                if x != t:
                    flag = False
            
            if flag is True:
                res.append(s)
                
        return res