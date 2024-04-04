class Solution:
    def maxDepth(self, s: str) -> int:
        ans = count = 0
        for x in s:
            if x == '(':
                count += 1
            if x == ')':
                ans = max(ans,count)
                count -= 1
        return ans