class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in findNums:
            res.append(-1)
            flag = False
            for i in range(len(nums)):
                if flag == False:
                    if nums[i] == x:
                        flag = True
                else:
                    if nums[i] > x:
                        res.pop()
                        res.append(nums[i])
                        break
        return res