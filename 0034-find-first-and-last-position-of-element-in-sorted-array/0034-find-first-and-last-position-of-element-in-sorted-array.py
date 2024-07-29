class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mi = -1
        ma = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                mi,ma = mid,mid
                while ma + 1 < len(nums) and nums[ma + 1] == target:
                    ma += 1
                while mi - 1 > -1 and nums[mi - 1] == target:
                    mi -= 1
                break  
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [mi,ma]
            
        