class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        ans = defaultdict(list)
        for x in strs:
            temp = ''.join(sorted(x))
            if temp not in ans:
                ans[temp] = []
            ans[temp].append(x)
                
        return list(ans.values())
    
        