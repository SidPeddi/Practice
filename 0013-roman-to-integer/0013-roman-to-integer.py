class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i,v in enumerate(s):
            if i and hashmap[s[i-1]] < hashmap[v]:
                total -= (2*(hashmap[s[i-1]]))
            total += hashmap[v]
        return total
        