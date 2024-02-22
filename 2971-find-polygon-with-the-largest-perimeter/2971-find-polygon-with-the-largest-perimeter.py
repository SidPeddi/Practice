class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while max(nums) >= sum(nums) - max(nums):
            nums.remove(max(nums))
            if not len(nums) >= 3:
                return -1
        return sum(nums)
