class Solution:
    def reverseWords(self, s: str) -> str:
        r = 0
        s = s.strip()
        ans = []
        start = 0
        s += ' '
        while r < len(s):
            if s[r].isalnum() == False and r < len(s):
                ans.append(s[start:r])
                while s[r] == ' ' and (r + 1) < len(s):
                    r += 1
                start = r
            r += 1
        ans = ans[::-1]
        return ' '.join(ans)
            
        