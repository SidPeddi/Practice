class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    left = mid + 1
            if mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1
            else:
                if nums[mid + 1] < nums[mid] > nums[mid - 1]:
                    return mid
                if nums[mid + 1] > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
                    
        