class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left, right = 0, len(nums)-1
        
        while left <= right:
            if nums[(left+right)//2] == target:
                return (left+right)//2
            elif nums[(left+right)//2] < target:
                left = (left+right)//2 + 1
            else:
                right = (left+right)//2 - 1
        return -1
    
nums = [2,5]
target = 5    
st = Solution()
print st.search(nums, target)