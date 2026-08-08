class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       #checking rows
        for i in range(9):
            row_set = set()
            for j in range(9):
                number = board[i][j]
                if number != ".":
                    if number in row_set:
                        return False
                    row_set.add(number)
        
        #checking columns
        for j in range(9):
            column_set = set()
            for i in range(9):
                number = board[i][j]
                if number != ".":
                    if number in column_set:
                        return False
                    column_set.add(number)
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])

        return True
