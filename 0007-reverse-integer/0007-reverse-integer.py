class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp = -1
            x = -x
        else:
            temp = 1
        ans = 0
        while x:
            ans *= 10
            ans += x % 10
            x = x // 10
        ans *= temp
        if ans <= -2 ** 31 or ans >= 2 ** 31 - 1:
            return 0
        return ans