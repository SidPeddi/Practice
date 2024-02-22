class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        hashset = set(jewels)
        maxcount = 0
        for c in stones:
            if c in hashset:
                maxcount += 1
        
        return maxcount