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
        
        temp = list(counts)
        for c in temp:
            if c in temp:
                while counts[c]:
                    ans.append(c)
                    counts[c] = counts.get(c,0) - 1
                del counts[c]
        return ''.join(ans)
                
                
                