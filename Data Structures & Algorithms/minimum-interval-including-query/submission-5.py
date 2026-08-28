class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        copy_query = queries
        resMap = {}
        intervals.sort()
        i = 0
        minHeap = []

        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            if minHeap:
                resMap[q] = minHeap[0][0]
            else:
                resMap[q] = -1
        
        return [resMap[q] for q in copy_query]