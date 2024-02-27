class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 1
        nums.sort()
        start = nums[0]
        for index, val in enumerate(nums):
            if val - start > k:
                start = val
                ans += 1
        return ans

        