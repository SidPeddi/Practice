class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        ans = []
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
                if len(temp) == c:
                    ans.append(temp)
                    temp = []
        return ans
        