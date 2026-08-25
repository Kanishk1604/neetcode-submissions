class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rowset[r] 
                or board[r][c] in colset[c] 
                or board[r][c] in boxset[(r // 3, c // 3)] 
                ):
                    return False

                rowset[r].add(board[r][c])
                colset[c].add(board[r][c])
                boxset[(r // 3, c //3)].add(board[r][c])

        return True