class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, word, visit):
            if ( i < 0 or j < 0 or i >= rows or j >= cols or board[i][j]!= word[0] or (i, j) in visit):
                return False
            visit.add((i, j))
            
            if len(word) == 1:
                return True
            res = (dfs(i + 1, j, word[1:], visit) 
                or dfs(i - 1, j, word[1:], visit) 
                or dfs(i, j + 1, word[1:], visit) 
                or dfs(i, j - 1, word[1:], visit))
                
            visit.remove((i, j))
            return res
            
        for r in range(rows):
            for c in range(cols):
                visit = set()
                if board[r][c] == word[0]:
                    if dfs(r, c, word, visit):
                        return True
        
        return False

