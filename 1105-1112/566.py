class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if (row*col)%r != 0:
            return nums
        tmp = []
        for i in range(row):
            for j in range(col):
                tmp.append(nums[i][j])
        res = []
        x = row * col / r
        for i in range(r):
            res.append(tmp[i*x:i*x+x])
        return res
    
    
nums = [[1,2],[3,4]]
print nums
r = 1
c = 4
st = Solution()
print st.matrixReshape(nums, r, c)