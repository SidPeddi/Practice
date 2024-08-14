class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def steps(m,n):
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            return steps(m-1,n) + steps(m,n-1)
        return steps(m,n)
        