class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def search(mid):
            ans = 0
            for x in candies:
                ans += floor(x / mid)
            return ans
        left = 0
        right = max(candies)
        while left < right:
            mid = (left + right + 1) // 2
            if search(mid) < k:
                right = mid - 1
            else:
                left = mid
        return left
        