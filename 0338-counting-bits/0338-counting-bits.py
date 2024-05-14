class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for x in range(0,n+1):
            count = 0
            while x:
                if x % 2:
                    count += 1
                x = x >> 1
            ans.append(count)
        return ans