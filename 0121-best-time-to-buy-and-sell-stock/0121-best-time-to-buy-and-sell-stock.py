class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        temp = prices[0]
        profit = 0
        for x in prices:
            if x < temp:
                temp = x
            profit = max(profit, x - temp)
        return profit