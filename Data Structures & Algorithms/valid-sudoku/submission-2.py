class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row = 1
        # col = 2
        # row and col 0,1,2 
        #   for i range 9
            #i = 6
        # boxcol =  (i % 3) * 3 + col
        # boxrow = row + (i//3) * 3

        rows, cols = len(board), len(board[0])

        for r in range(rows):
            row_seen = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_seen:
                    return False  
                row_seen.add(board[r][c])

        for c in range(cols):
            col_seen = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in col_seen:
                    return False  
                col_seen.add(board[r][c])
        
        for i in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (i//3) * 3 + r
                    col = (i%3) * 3 + c

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True
                
