class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sus = 0
        for x in range(1,len(nums)+1):
            sus += x
        return sus - sum(nums)