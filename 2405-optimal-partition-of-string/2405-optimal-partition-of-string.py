class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = set()
        counter = 1

        for val in s:
            if val in map:
                counter += 1
                map = set()
            map.add(val)
            
        return counter