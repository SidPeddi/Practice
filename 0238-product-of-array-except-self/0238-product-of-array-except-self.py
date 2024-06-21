class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        for x in range(1,len(nums)):
            prefix[x] = nums[x-1] * prefix[x-1]
        nums = nums[::-1]
        for x in range(1, len(nums)):
            postfix[x] = nums[x-1] * postfix[x-1]
        postfix = postfix[::-1]
        for x in range(len(nums)):
            prefix[x] *= postfix[x]
        return prefix