class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for s in A:
            for i in range(len(s)/2):
                tmp = s[i]
                s[i] = (1^s[len(s)-1-i])
                s[len(s)-1-i] = (1^tmp)
            if len(s)%2 != 0:
                s[len(s)/2] = s[len(s)/2]^1
        return A