class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for s in words:
            tmp = ''
            for i in range(len(s)):
                tmp += ref[ord(s[i])-97]
            if tmp in result:
                pass
            else:
                result.append(tmp)
        return len(result)