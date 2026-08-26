class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x, y = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x - x2) + abs(y - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = [(0, 0)]
        visit = set()
        cost = 0
        while len(visit) < N:
            d, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)

            cost += d

            for neiCost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiCost, nei))
        
        return cost

