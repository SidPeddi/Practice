class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        
        Hash = {}
        doubleset = set()
        ans = 0
        for x in words:
            if Hash.get(x[::-1]):
                ans += 4
                Hash[x[::-1]] = Hash.get(x[::-1],0) - 1
            else:
                Hash[x] = Hash.get(x,0) + 1
            if x[::-1] == x:
                if x in doubleset:
                    doubleset.remove(x)
                else:
                    doubleset.add(x)
        if doubleset:
            ans += 2
        return ans 
                
                
        