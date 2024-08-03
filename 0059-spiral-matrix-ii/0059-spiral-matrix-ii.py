class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        t = 0
        r = n
        b = n
        l = 0
        i = 1
        while l < r and t < b:
            for x in range(l,r):
                matrix[t][x] = i
                i += 1
            t += 1
            for x in range(t,b):
                matrix[x][r-1] = i
                i += 1
            r -= 1
            for x in range(r-1,l-1,-1):
                matrix[b-1][x] = i
                i += 1
            b -= 1
            for x in range(b-1,t-1,-1):
                matrix[x][l] = i
                i += 1
            l += 1

        return matrix