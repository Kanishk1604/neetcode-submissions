class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append((v,w))
        
        visit = set()
        time = 0
        minheap = [(0, k)]

        while minheap:
            val = heapq.heappop(minheap)

            if val[1] in visit:
                continue
            
            visit.add(val[1])
            time = val[0]

            for nei in adj[val[1]]:
                if nei not in visit:
                    heapq.heappush(minheap, (nei[1] + time, nei[0]))
        
        return time if len(visit) == n else -1