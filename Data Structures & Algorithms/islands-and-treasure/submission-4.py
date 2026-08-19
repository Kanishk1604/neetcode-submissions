class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for d1, d2 in directions:
                    x1 = x + d1
                    y1 = y + d2
                    if (x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and grid[x1][y1] == 2147483647):
                        grid[x1][y1] = grid[x][y] + 1
                        q.append([x1, y1])
        
