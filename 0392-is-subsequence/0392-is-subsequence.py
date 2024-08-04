class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) >= len(t):
            return s == t
        i = 0
        x = 0
        while x < len(t) and i < len(s):
            if t[x] == s[i]:
                i += 1
            x += 1
        return i == len(s)
        