class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        res = []
        for x in range(len(nums)-1, -1, -1):
            if abs(nums[x]) > abs(nums[l]):
                res.append(nums[x])
            else: 
                res.append(abs(nums[l]))
                nums.pop(0)
        res = res[::-1]
        for x in range(len(res)):
            res[x] *= res[x]
        return res
                
                