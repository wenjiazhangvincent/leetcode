class Solution(object):
    def tra(self,a):
        if not a:
            return 
        A = []
        for i in range(2):
            A.append(a[i::2])
            A[i].sort()
        return A
        
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = []
        for s in A:
            tmp = [] 
            for c in s:
                tmp.append(ord(c)-97)
            tmp = self.tra(tmp)
            if not tmp in res:
                res.append(tmp)
        return len(res)