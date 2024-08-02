class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def cols(board):
            for x in range(9):
                newset = set()
                for i in range(9):
                    if board[x][i] != '.':
                        if board[x][i] in newset:
                            return False
                        else:
                            newset.add(board[x][i])
            return True
        def rows(board):
            for x in range(9):
                newset = set()
                for i in range(9):
                    if board[i][x] != '.':
                        if board[i][x] not in newset:
                            newset.add(board[i][x])
                        else:
                            return False
            return True
        def box(board,y,j):
            newset = set()
            for x in range(3):
                for i in range(3):
                    if board[y + x][j + i] != '.':
                        if board[y + x][j + i] not in newset:
                            newset.add(board[y + x][j + i])
                        else:
                            return False
            return True
        for x in range(3):
            for y in range(3):
                if box(board,x*3,y*3) == False:
                    return False
        return rows(board) and cols(board)
        