class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        small = prices[0]
        profit = 0

        for x in prices:
            if x < small:
                small = x
            profit = max(profit, x-small)
        return profit