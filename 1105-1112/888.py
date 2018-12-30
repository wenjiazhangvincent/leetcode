class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = (sum(A) - sum(B)) / 2
        A = [x - d for x in A]
        res = list(set(A) & set(B))[0]
        return [res+d,res]