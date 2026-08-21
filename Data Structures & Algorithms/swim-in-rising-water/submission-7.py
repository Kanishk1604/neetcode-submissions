class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()

        minHeap = [[grid[0][0], 0, 0]]
        dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while (n-1, n-1) not in visited:
            t, x, y = heapq.heappop(minHeap)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            time = t

            for d1, d2 in dir:
                x2 = x + d1
                y2 = y + d2
                if (x2 < 0 or x2 >= n or y2 < 0 or y2 >= n or grid[x2][y2] in visited):
                    continue
                maxtime = max(time, grid[x2][y2])
                heapq.heappush(minHeap, (maxtime, x2, y2))
        
        return time