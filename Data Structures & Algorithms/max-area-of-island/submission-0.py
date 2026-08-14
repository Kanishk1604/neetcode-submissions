class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i: int, j: int, m: int, n: int, grid: List[List[int]]) -> int:
            res = 1
            if (i >=0 and i < m and j >= 0 and j < n and grid[i][j] == 1):
                grid[i][j] = 0
            else:
                 return 0
            
            res += dfs(i + 1, j, m, n, grid) + dfs(i - 1, j, m, n, grid) + dfs(i, j + 1, m, n, grid) + dfs(i, j - 1, m, n, grid) 

            return res

        m = len(grid)
        n = len(grid[0])
        maxarea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, m, n, grid)
                    maxarea = max(maxarea, area)
                
        return maxarea

        
