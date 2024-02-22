class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = set()
        for i in s:
            if i in map:
                return i
            map.add(i)
        