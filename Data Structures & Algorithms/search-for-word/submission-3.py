class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, m, n, word, visit):
            if not word:
                return True
            visited = str(i) + str(j)
            if (i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0] or visited in visit):
                return False
            visit.add(visited)
            res = (dfs(i + 1, j, m, n, word[1:], visit)
            or dfs(i - 1, j, m, n, word[1:], visit)
            or dfs(i, j + 1, m, n, word[1:], visit)
            or dfs(i, j - 1, m, n, word[1:], visit))
            visit.remove(visited)
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visit = set()
                    if (dfs(r, c, m, n, word, visit)):
                        return True
        return False
        