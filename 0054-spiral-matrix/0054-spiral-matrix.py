class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t = 0
        b = len(matrix)
        l = 0
        r = len(matrix[0])
        ans = []
        while l < r and t < b:
            
            for x in range(l,r):
                ans.append(matrix[t][x])
            t += 1
            
            for x in range(t,b):
                ans.append(matrix[x][r-1])
            r -= 1
            if not (l < r and t < b):
                break
            for x in range(r-1,l-1,-1):
                ans.append(matrix[b-1][x])
            b -= 1
            for x in range(b-1,t-1,-1):
                ans.append(matrix[x][l])
            l += 1
        return ans
        