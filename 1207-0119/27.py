class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return nums
    
nums = [3,2,2,3]
val = 3
st = Solution()
print st.removeElement(nums, val)