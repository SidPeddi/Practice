class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = defaultdict(list)

        for x in range(len(strs)):
            key = ''.join(sorted(strs[x]))
            map[key].append(strs[x])
        return map.values()