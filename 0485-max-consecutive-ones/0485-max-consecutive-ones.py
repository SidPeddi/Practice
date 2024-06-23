class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for x in nums:
            if x:
                count += 1
            else:
                res = max(res,count)
                count = 0
                
        return max(res,count)