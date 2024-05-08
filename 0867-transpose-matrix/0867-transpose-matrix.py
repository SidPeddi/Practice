class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            tot = []
            for j in range(len(matrix)):
                print(i,j, matrix[j][i])
                tot.append(matrix[j][i])
            ans.append(tot)
            
        return ans
        