class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}

        for src, dst, t in times:
            adj[src].append((t, dst))

        visit = set()
        minHeap = [(0, k)]
        time = 0
        while minHeap:
            t, src = heapq.heappop(minHeap)
            if src in visit:
                continue
            visit.add(src)
            time = t

            for neiTime, nei in adj[src]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiTime + time, nei))
        
        return time if len(visit) == n else -1