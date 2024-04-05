class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def conditional(val):
            hours = 0
            for x in piles:
                hours += math.ceil(x/val)
            return hours <= h 
                
            
            
            
        left,right = 1, max(piles)
        while left < right:
            mid = left + (right-left) // 2
            if conditional(mid):
                right = mid
            else:
                left = mid + 1
        return left