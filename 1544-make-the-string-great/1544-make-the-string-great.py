class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        i = 0
        while i + 1 < len(s):
            if s[i] != s[i+1]:
                if s[i].upper() == s[i+1].upper():
                    s.pop(i)
                    s.pop(i)
                    i = -1
                    
            i += 1
        return "".join(s)