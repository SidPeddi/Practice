class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hashmap = {}
        doubleset = set()
        count = 0
        ans = 0
        for x in words:
            if x[::-1] == x:
                if x in doubleset:
                    doubleset.remove(x)
                    ans += 4
                else:
                    doubleset.add(x)
            elif x[::-1] in hashmap:
                if hashmap[x[::-1]] == 1:
                    del hashmap[x[::-1]]
                else:
                    hashmap[x[::-1]] -= 1
                ans += 4
            else:
                hashmap[x] = hashmap.get(x,0) + 1
        if doubleset:
            count = 2
        print(count)
        return ans + count
                
                
        