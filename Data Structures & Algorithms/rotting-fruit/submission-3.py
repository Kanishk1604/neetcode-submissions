class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [[1,0], [-1,0], [0,1], [0, -1]]
        q = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
                for d1, d2 in dir:
                    x2 = x + d1
                    y2 = y + d2
                    if (x2 >= 0 and x2 < m and y2 >= 0 and y2 < n and grid[x2][y2] == 1):
                        fresh -= 1
                        grid[x2][y2] = 2
                        q.append([x2, y2])
            time += 1
        
        return time if fresh == 0 else -1