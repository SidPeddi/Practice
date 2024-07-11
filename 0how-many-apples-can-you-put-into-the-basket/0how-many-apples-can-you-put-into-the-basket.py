class Solution(object):
    def maxNumberOfApples(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        weight.sort()
        basket = 5000
        x = 0
        while basket and x < len(weight):
            if (basket - weight[x]) >= 0:
                basket -= weight[x]
            else:
                return x
            x += 1
        return x 