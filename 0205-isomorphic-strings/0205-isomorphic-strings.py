class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in range(len(s)):
            map1.append(s.index(s[idx]))
            map2.append(t.index(t[idx]))
        return map1 == map2