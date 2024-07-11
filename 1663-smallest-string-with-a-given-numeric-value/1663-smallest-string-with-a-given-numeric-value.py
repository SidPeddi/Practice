class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ['a'] * n
        val = n
        
        for x in range(n-1,-1,-1):
            if k == val:
                break
            val -= 1
            ans[x] = chr(96 + min(k - val, 26))
            val += ord(ans[x]) - 96
        
        return ''.join(ans)
            