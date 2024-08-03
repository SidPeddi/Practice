class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return matrix
        n = len(matrix)
        if n == 2:
            n = 3
        for i in range(n - 2):
            x = 0
            t = 0 + i
            b = len(matrix) - 1 - i 
            l = 0 + i
            r = len(matrix) - 1 - i
            while x < (r-l):
                temp = matrix[t+x][l]
            
                matrix[t+x][l] = matrix[b][l+x]
            
                matrix[b][l+x] = matrix[b-x][r]
            
                matrix[b-x][r] = matrix[t][r-x]
                
                matrix[t][r-x] = temp
                x += 1
        return matrix
        
        