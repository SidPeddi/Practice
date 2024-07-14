class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        ans = ''
        for c in order:
            while counts[c]:
                ans += c
                counts[c] -= 1
            s = s.replace(c, '')
        return ans + s
                
                
                