class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        val = 1
        l = 0
        r = n
        top = 0
        bottom = n
        while l < r:
            for x in range(l,r):
                ans[top][x] = val
                val += 1
            top += 1
            for i in range(top, bottom):
                ans[i][r-1] = val
                val += 1
            r -= 1
            for i in range(r-1,l-1,-1):
                ans[bottom-1][i] = val
                val += 1
            bottom -= 1
            for i in range(bottom-1,top-1,-1):
                ans[i][l] = val
                val += 1
            l += 1
        
        return ans