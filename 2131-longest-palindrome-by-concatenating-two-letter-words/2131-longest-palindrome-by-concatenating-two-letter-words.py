class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        maps = {}
        count = 0
        for x in words:
            if x[::-1] in maps:
                print(x)
                count += 4
                maps[x[::-1]] = maps.get(x[::-1],0) - 1
                if maps[x[::-1]] == 0:
                    del maps[x[::-1]]
            else:
                maps[x] = maps.get(x,0) + 1
        for x in words:
            if x in maps:
                if x == x[::-1]:
                    print(x)
                    count += 2
                    break
        return count
        