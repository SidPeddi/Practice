class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        esum = len(nums) * (len(nums)+1) / 2
        return esum - sum(nums)
        