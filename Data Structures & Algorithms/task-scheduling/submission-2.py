class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}

        for task in tasks:
            freqMap[task] = 1 + freqMap.get(task, 0)

        maxHeap = [-t for t in freqMap.values()] 
        heapq.heapify(maxHeap)
        q = deque() #stores tiem and cpu
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append((time + n, count))
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])
        
        return time

