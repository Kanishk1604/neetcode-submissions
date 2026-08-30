class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset = set()
        posDiag = set()
        negDiag = set()
        res = []
        
        board = [["."] * n for i in range(n)] 
        # board = [["."] * n] * n 

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return 
            
            for c in range(n):
                if c in colset or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                
                board[r][c] = "Q"
                colset.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                dfs(r + 1)

                board[r][c] = "."
                colset.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        
        dfs(0)
        return res
                
        