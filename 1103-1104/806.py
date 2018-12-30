class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        units = 0
        for i in range(len(S)):
            units += widths[ord(S[i])-97]
            if units > 100:
                units = widths[ord(S[i])-97]
                lines += 1
        return [lines,units]