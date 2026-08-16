class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}

        for num in nums:
            freqmap[num] = 1 + freqmap.get(num, 0)

        minheap = []

        for key, val in freqmap.items():
            heapq.heappush(minheap, (val,key))

            if (len(minheap) > k):
                heapq.heappop(minheap)
        
        res = []
        while minheap:
            freq, num = heapq.heappop(minheap)
            res.append(num)

        return res