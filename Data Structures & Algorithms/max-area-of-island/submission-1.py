class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, grid) -> int:
            res = 1
            if (i >=0 and i < m and j >= 0 and j < n and grid[i][j] == 1):
                grid[i][j] = 0
            else:
                 return 0
            
            res += dfs(i + 1, j, grid) + dfs(i - 1, j, grid) + dfs(i, j + 1, grid) + dfs(i, j - 1, grid) 

            return res

        
        maxarea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, grid)
                    maxarea = max(maxarea, area)
                
        return maxarea

        
