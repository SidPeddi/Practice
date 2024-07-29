class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 1
        for x in range(1,n+1):
            ans *= x
        count = 0
        while ans % 10 == 0:
            count += 1
            ans //= 10
        return count
            
        