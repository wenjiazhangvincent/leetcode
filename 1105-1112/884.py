class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(' ')
        b = B.split(' ')
        tmp = {}
        for s in a:
            if tmp.get(s):
                tmp[s] += 1
            else:
                tmp[s] = 1
        for s in b:
            if tmp.get(s):
                tmp[s] += 1
            else:
                tmp[s] = 1
        res = []
        for k,v in tmp.items():
            if v == 1:
                res.append(k)
        
        return res