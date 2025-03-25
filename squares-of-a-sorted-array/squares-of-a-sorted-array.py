class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0 
        r = len(nums) -1 
        ans = []
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                ans.append(nums[l] * nums[l])
                l += 1
            else:
                ans.append(nums[r] * nums[r])
                r -= 1
        return ans[::-1]
                