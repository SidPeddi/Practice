class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerosr = set()
        zerosc = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zerosr.add(r)
                    zerosc.add(c)
        while zerosr:
            temp = zerosr.pop()
            for c in range(len(matrix[0])):
                matrix[temp][c] = 0
        while zerosc:
            temp = zerosc.pop()
            for r in range(len(matrix)):
                matrix[r][temp] = 0
        return
        