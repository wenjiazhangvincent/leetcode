class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = q = 0
        res = 0
        tmp = 0
        flag = False
        while p < len(prices) - 1:
            if flag:
                if q < len(prices) - 1:
                    if prices[q+1] > prices[q]:
                        q += 1
                    else:
                        res += prices[q] - prices[p]
                        flag = False
                        p = q + 1
                else:
                    res += prices[q] - prices[p]
                    break
            else:
                if prices[p+1] > prices[p]:
                    q = p + 1
                    tmp = prices[p+1] - prices[p]
                    flag = True
                else:
                    p += 1
        return res