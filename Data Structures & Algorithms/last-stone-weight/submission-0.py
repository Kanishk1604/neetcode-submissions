class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for num in stones:
            heapq.heappush(maxHeap, -num)
        
        while len(maxHeap) >= 2:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            diff = x - y
            if (diff) != 0:
                heapq.heappush(maxHeap, -diff)
        
        return -maxHeap[0] if len(maxHeap) == 1 else 0