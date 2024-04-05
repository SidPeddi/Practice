class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(val):
            total = 0
            count = 1
            for x in weights:
                total += x
                if total > val:
                    total = x
                    count += 1
                if count > days:
                    return False
            return True
                
                           
                
                
        left, right = max(weights),sum(weights) 
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        