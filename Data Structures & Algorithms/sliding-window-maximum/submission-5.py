class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #[1 2 1 3 1 1 1]
        # 2
        # 3
        # 3
        # 3
        
        #popping all from maxheap whose index < l        
        maxHeap = []
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        l = 1
        r = k
        res = []
        res.append(-maxHeap[0][0])
        while r < len(nums):
            while maxHeap and maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
            
            heapq.heappush(maxHeap, (-nums[r], r))
            res.append(-maxHeap[0][0])
            r += 1
            l += 1
        
        return res
            
        
        


