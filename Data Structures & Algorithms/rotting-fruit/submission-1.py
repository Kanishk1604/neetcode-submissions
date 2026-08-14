class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
        
        visit = set()
        minutes = 0
        while queue:
            lvl = len(queue)
            for i in range(lvl):
                cell = queue.popleft()
                for dir in direction:
                    x = cell[0] + dir[0]
                    y = cell[1] + dir[1]

                    if (x >= 0 and x < rows and y >= 0 and y < cols and (x,y) not in visit and grid[x][y] == 1):
                        grid[x][y] = 2
                        visit.add((x,y))
                        queue.append([x,y])
            if queue:
                minutes += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return minutes