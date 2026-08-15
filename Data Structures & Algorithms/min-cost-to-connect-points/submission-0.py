class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}

        for i in range(n):
            x, y = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x-x2) + abs(y-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        minheap = [(0, 0)]
        visit = set()
        total_cost = 0

        while len(visit) < n:
            cost, i = heapq.heappop(minheap)
            if i in visit:
                continue
            visit.add(i)
            
            total_cost += cost
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap, (neiCost, nei))

        return total_cost
