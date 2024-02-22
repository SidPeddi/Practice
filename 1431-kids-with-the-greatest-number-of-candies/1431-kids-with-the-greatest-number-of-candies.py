class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
 
        temp = max(candies)
        for x in range(len(candies)):
            if candies[x] + extraCandies < temp:
                 candies[x] = 0
        return candies
        