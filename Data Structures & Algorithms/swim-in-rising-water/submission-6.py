class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #start from (0,0)
        #add to minheap (0,0)
        # visit
        #time
        # while last element not in visit
        #pop x, y 
        #time = max(time,grid[x][y])
        #look in right and bott dir
        #add to minheap
        # repeat loop

        minheap = [(grid[0][0],(0,0))]
        time = 0
        visit = set()
        n = len(grid)
        dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        while ((n-1, n-1)) not in visit:
            t , node = heapq.heappop(minheap)
            x = node[0]
            y = node[1]
            if (x,y) in visit:
                continue
            visit.add((x, y))
            time = t
            
            for d in dir:
                x2 = x + d[0]
                y2 = y + d[1]
                if (x2 < n and y2 < n and x2 >= 0 and y2 >= 0):
                    max_time = max(t, grid[x2][y2])
                    if ((x2, y2)) not in visit:
                        heapq.heappush(minheap, (max_time, (x2, y2)) )
            
        return time
            
            