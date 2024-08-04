class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [[]for _ in range(numRows)]

        index = 0
        step = -1
        for char in s:
            res[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join([''.join(map(str, row)) for row in res])
    
                
            
            
        