class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxHeap = []

        for w in stones:
            heapq.heappush(maxHeap, -w)

        while maxHeap and len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            diff = y - x
            if diff > 0:
                heapq.heappush(maxHeap, -diff)
        
        if maxHeap:
            return -maxHeap[0]
        return 0