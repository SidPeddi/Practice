class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix = [nums[0]]
        tot = 0
        if (2*k+1) > len(nums):
            return [-1] * len(nums)
        for x in range(1, len(nums)):
            prefix.append(nums[x] + prefix[-1])
        arr = []

        for x in range(len(nums)):
            if x < k or x >= len(nums)-k:
                arr.append(-1)
            else:
                arr.append((prefix[x + k] - tot)// (2*k+1))

                tot = prefix[x-k]
        return arr