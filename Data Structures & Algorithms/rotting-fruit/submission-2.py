class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i,j])
        
        minutes = 0
        while fresh > 0 and queue:
            lvl = len(queue)
            for i in range(lvl):
                cell = queue.popleft()
                for dir in direction:
                    x = cell[0] + dir[0]
                    y = cell[1] + dir[1]
                    if (x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] == 1):
                        grid[x][y] = 2
                        queue.append([x,y])
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1