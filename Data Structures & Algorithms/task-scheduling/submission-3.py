class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        countMap = {}
        for t in tasks:
            countMap[t] = 1 + countMap.get(t, 0)
        
        maxHeap = []

        for t in countMap.values():
            heapq.heappush(maxHeap, -t)

        q = deque()
        time = 0

        while maxHeap or q:

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((time + n, cnt))
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])
            time += 1
        
        return time
                
