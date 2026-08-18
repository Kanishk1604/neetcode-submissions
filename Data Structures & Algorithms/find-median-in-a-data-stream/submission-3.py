class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    #[1,2,3,4]
    #small  - [-4, -3, -2, -1]
    #large - [5, 6, 7]
    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num) #maxheap

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        elif len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) != len(self.large):
            if len(self.small) < len(self.large):
                return self.large[0]
            else:
                return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        