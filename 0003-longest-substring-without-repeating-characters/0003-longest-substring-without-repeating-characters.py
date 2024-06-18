class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        hashmap = set()
        ans = 0
        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
            ans = max(ans, r-l+1)
            hashmap.add(s[r])
        return ans
