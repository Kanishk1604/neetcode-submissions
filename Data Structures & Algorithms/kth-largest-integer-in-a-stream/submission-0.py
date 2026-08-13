class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []

        for num in self.nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        
        count = 0
        temp_list = []
        while count != self.k - 1:
            temp_list.append(-heapq.heappop(self.heap))
            count += 1
            
        res = -self.heap[0]

        for num in temp_list:
            heapq.heappush(self.heap, -num)

        return res
        
