class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]
        for x in range(len(gain)):
            ans.append(ans[x] + gain[x])
        print(ans)
        return max(ans)
        