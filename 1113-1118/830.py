class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i = 0
        res = []
        while i < len(S) - 2:
            if S[i+1] == S[i]:
                j = i + 2
                while S[j] == S[i]:
                    j += 1
                    if j >= len(S):
                        break
                if j-i > 2:
                    res.append([i,j-1])
                i = j
            else:
                i += 1
        return res
            