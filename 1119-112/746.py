class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in xrange(2, len(cost)):
            cost[i]+= min(cost[i-1], cost[i-2])
        return min(cost[-1],cost[-2])
    
st = Solution()
cost =  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print st.minCostClimbingStairs(cost)