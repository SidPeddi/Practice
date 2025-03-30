class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for x in range(1,len(nums)):
            res.append(nums[x]+res[-1])
        return res
    

        