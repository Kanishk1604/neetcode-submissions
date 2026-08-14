class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        res = 0
        for num in nums:
            heapq.heappush(maxheap, -num)

        while k > 0:
            res = -heapq.heappop(maxheap)
            k -= 1
        
        return res