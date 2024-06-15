class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        ans = 0
        for x in numset:
            if (x-1) not in numset:
                num = x + 1
                while num in numset:
                    num += 1
                ans = max(ans, num - x)
        return ans

        