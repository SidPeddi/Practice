class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        
        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2) + climb(n-3)
                return memo[n]
        return climb(n)
        