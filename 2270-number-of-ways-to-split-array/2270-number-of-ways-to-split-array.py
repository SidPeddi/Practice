class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        prefix = [nums[0]]
        for x in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[x])
        for x in range(len(prefix)-1):
            if prefix[x] >= (prefix[-1] - prefix[x]):
                count += 1
        return count
        