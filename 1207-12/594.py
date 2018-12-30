import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        dct = collections.Counter(nums)
        if len(dct) == 1:
            return 0
        
        st = set(nums)
        res = 0
        for i,cnt in dct.items():
            if i+1 in st:
                res = max(res, cnt+dct[i+1])
            elif i-1 in st:
                res = max(res, cnt+dct[i-1])
        return res

            
        
                
    
nums = [1,3,2,2,5,2,3,7] # 1 2 2 2 3 3 5 7
nums = [1,1,1]
st = Solution()
print st.findLHS(nums)
        
                