class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpset = Counter(s)
        for x in range(len(s)):
            if alpset[s[x]] == 1:
                return x
        return -1
        