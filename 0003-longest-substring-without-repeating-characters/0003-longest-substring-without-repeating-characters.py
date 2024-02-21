class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        left = 0
        map = {}

        for i,val in enumerate(s):
            if val in map:
                left = max(left, map[val])
            count = max (count, i - left + 1 )   
            map[val] = i + 1
        return count
                
