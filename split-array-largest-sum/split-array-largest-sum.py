class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(val):
            total = 0
            count = 1
            for x in nums:
                total += x
                if total > val:
                    total = x
                    count += 1
                    if count > k:
                        return False
            return True
                
                           
                
                
        left, right = max(nums),sum(nums) 
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        