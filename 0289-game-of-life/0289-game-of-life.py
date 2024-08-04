class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def current(r,c):
            return (0 <= r < len(board)) and (0 <= c < len(board[0]))                
        maps = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        toChange = {}
        liveCount = 0
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                liveCount = 0
                for dr,dc in maps:
                    if current(r + dr,c + dc) and board[r + dr][c + dc] == 1:
                            liveCount += 1
                if board[r][c] == 1:
                    if liveCount < 2 or liveCount > 3:
                        toChange[(r, c)] = 0
                else:
                    if liveCount == 3:
                        toChange[(r, c)] = 1
        
        
        
        for (r, c), nextState in toChange.items():
            board[r][c] = nextState