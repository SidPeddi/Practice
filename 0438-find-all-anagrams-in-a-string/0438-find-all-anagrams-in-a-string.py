class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r = len(p)
        count = Counter(p)
        ans = []
        for l in range(len(s) - len(p) + 1):
            if Counter(s[l:r+l]) == count:
                ans.append(l)
        return ans
        