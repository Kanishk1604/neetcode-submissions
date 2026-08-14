class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for point in points:
            eu_distance = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
            heapq.heappush(minHeap, (eu_distance, point))
        
        while k >0:
            closest_point = heapq.heappop(minHeap)
            res.append(closest_point[1])
            k -= 1
        
        return res