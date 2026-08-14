class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j])
        visited = set()

        while queue:
            cell = queue.popleft()
            for d in dir:
                new_cell = [cell[0] + d[0], cell[1] + d[1]]
                x = new_cell[0]
                y = new_cell[1]
                if (x >=0 and x < rows and y >= 0 and y < cols and(x,y) not in visited and grid[x][y] > 0):
                    grid[x][y] = grid[cell[0]][cell[1]] + 1
                    queue.append([x,y])
                    visited.add((x,y))
        
