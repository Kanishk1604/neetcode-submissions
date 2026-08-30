class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(i, j, visit, word):
            
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visit or board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True
            visit.add((i, j))
            res = (dfs(i + 1, j, visit, word[1:])
            or dfs(i - 1, j, visit, word[1:])
            or dfs(i, j + 1, visit, word[1:])
            or dfs(i, j - 1, visit, word[1:]))

            visit.remove((i, j))
            return res
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, visit, word):
                        return True
        
        return False

