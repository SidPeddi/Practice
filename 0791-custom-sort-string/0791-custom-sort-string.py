class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        ans = []
        for c in order:
            if c in counts:
                while counts[c]:
                    ans.append(c)
                    counts[c] = counts.get(c,0) - 1
                del counts[c]
                s = s.replace(c, '')
        temp = ''.join(ans)
        temp += s
        return temp
                
                
                