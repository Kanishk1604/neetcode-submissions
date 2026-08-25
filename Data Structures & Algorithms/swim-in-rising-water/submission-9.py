class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minHeap = [(grid[0][0], 0, 0)]
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        time = 0
        n = len(grid)
        while (n-1, n-1) not in visit:
            t, x, y = heapq.heappop(minHeap)

            if (x, y) in visit:
                continue
            visit.add((x, y))

            time = t

            for d1, d2 in dir:
                x2 = x + d1
                y2 = y + d2

                if (x2 < 0 or x2 >= n or y2 < 0 or y2 >= n or grid[x2][y2] in visit):
                    continue
                heapq.heappush(minHeap, (max(time, grid[x2][y2]), x2, y2))
        
        return time
