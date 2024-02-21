class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = l = 0
        map = {}

        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            
            while (r - l + 1) - max(map.values()) > k:
                map[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

        