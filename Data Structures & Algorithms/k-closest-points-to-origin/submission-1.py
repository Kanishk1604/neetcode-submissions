class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            heapq.heappush(maxHeap, (-math.sqrt(x ** 2 + y ** 2), [x, y]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])

        return res