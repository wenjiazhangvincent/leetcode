class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        p, q = 0, len(nums)-1
        while nums[(p+q)/2] != target and p < q:
            if nums[(p+q)/2] > target:
                q = (p+q)/2 - 1
            else:
                p = (p+q)/2 + 1
        if nums[(p+q)/2] >= target:
            return max(0, (p+q)/2)
        else:
            return (p+q)/2 + 1