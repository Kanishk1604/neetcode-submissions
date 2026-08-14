class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(i, j, m, n, grid)
        
        return res

    def dfs(self, i: int, j: int, m: int, n: int, grid: List[List[str]]):
        if (i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == "1"):
            grid[i][j] = "0"
        else:
            return

        self.dfs(i + 1, j, m, n, grid)
        self.dfs(i - 1, j, m, n, grid)
        self.dfs(i, j + 1, m, n, grid)
        self.dfs(i, j - 1, m, n, grid)

            