class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)
        
        def search(speed):
            ans = 0
            for x in piles:
                ans += ceil(x/speed)
            return ans
        
        
        while left <= right:
            mid = (right + left) // 2

            if search(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left