class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def choose(mid):
            ans = 0
            for x in piles:
                ans += ceil(x/mid)
            return ans
        
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if choose(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left
        