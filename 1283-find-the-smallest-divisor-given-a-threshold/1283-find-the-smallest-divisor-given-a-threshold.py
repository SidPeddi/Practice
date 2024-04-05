class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(divisor) -> bool:
            total = 0
            for x in nums:
                total += math.ceil(x / divisor)
            if total <= threshold:
                return divisor

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left