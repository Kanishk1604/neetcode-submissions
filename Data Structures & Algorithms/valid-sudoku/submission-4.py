class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowset[row]
                or board[row][col] in colset[col]
                or board[row][col] in boxset[(row // 3, col //3)]
                ):
                    return False
                rowset[row].add(board[row][col])
                colset[col].add(board[row][col])
                boxset[(row // 3, col //3)].add(board[row][col])
        
        return True