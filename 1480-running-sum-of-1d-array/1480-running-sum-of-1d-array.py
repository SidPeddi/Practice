class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        for x in range(1, len(nums)):
            prefix.append(nums[x] + prefix[-1])
        return prefix