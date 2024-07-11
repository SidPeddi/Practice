class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0
        length = len(t)
        for c in s:
            if i >= len(t):
                return length
            if c == t[i]:
                length -= 1
                i += 1
        return length