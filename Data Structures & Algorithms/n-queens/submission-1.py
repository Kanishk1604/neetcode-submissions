class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in colset or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                colset.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                colset.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
                