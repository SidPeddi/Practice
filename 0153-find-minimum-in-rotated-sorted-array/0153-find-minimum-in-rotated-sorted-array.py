class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minnum = nums[left]
        while left <= right:
            mid = (left + right) // 2
            minnum = min(minnum,nums[mid])
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        return minnum
        