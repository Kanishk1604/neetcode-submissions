class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}

        for n1, n2, time in times:
            adj[n1].append((n2, time))

        minHeap = [(0, k)]
        mintime = float("inf")
        visited = set()
        while minHeap:     
            t, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            visited.add(src)
            mintime = t

            for dst, dstTime in adj[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (t + dstTime, dst))
        
        return mintime if len(visited) == n else -1


