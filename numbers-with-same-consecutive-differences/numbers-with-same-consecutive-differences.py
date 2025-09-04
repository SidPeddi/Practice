class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtacking(curr):
            if len(curr) == n:
                ans.append(int("".join(map(str, curr[:]))))
                return
            
            for x in {curr[-1]-k, curr[-1]+k}:
                if 0 <= x <= 9:
                    curr.append(x)
                    backtacking(curr)
                    curr.pop()
        ans = []
        for i in range(1,10):
            backtacking([i])
        return ans