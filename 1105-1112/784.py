class Solution:
    def letterCasePermutation(self, S):
        ret = {''}
        for s in S:
            ret = {r + t for r in ret for t in (s.lower(), s.upper())}
        return list(ret)
    
st = Solution()
S = '1a2B'
print st.letterCasePermutation(S)