class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for x in nums:
            if x == 1:
                count += 1
            if x == 0:
                res = max(res,count)
                count = 0
                
        return max(res,count)