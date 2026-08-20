class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        notSurrounded = set()

        def dfs(i, j):
            if (i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] == "X" or (i, j) in notSurrounded):
                return 
            notSurrounded.add((i, j))
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
 
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in notSurrounded:
                    board[r][c] = "X"
