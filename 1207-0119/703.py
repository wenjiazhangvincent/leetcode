class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.nums = nums[-k:]
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
#         if len(self.nums) < self.k:
#             self.nums.append(val)
#             self.nums.sort()
#         elif val > self.nums[0]:
#             self.nums.pop(0)
#             self.nums.append(val)
#             self.nums.sort()
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

k = 1  
nums = [1]
st = KthLargest(k, nums)
