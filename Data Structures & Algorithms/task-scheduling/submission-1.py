class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # [A, A, A, B, B, C, C]
        # (-3, -2, -2)
        #(A,4) (B,5) (C, 6) (A,8)
        # A - B - C - idle - A - B - C - idle - A

       
        freqMap = {}
        for task in tasks:
            freqMap[task] = 1 + freqMap.get(task, 0)
        maxHeap = [-cnt for cnt in freqMap.values()]
        heapq.heapify(maxHeap)
        q = deque() #count, idletime
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 +heapq.heappop(maxHeap)
                if count:
                    q.append((count, n + time))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
           



        
