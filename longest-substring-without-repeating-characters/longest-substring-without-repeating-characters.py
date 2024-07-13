class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mapset = {}
        maxlen = 0
        for r in range(len(s)):
            if s[r] in mapset:
                l = max(mapset[s[r]], l)
            maxlen = max(maxlen, r - l  + 1)

            mapset[s[r]] = r + 1
        return maxlen
            

                
            