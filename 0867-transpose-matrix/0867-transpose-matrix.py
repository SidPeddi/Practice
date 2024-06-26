class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0]* len(matrix) for _ in range(len(matrix[0]))]
        for x in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][x]= matrix[x][j]
        return ans