class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p, q = 0, len(numbers)-1
        while p < q:
            tmp = numbers[p] + numbers[q]
            if  tmp == target:
                return [p+1, q+1]
            elif tmp < target:
                p += 1
            else:
                q -= 1  
            
            