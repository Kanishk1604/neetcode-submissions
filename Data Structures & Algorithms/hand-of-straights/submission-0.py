class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize: 
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minHeap = []
        for key in count:
            heapq.heappush(minHeap, key)
        
        while minHeap:
            smallest = minHeap[0]  
            for i in range(smallest, smallest + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if not minHeap or minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)    
        return True
        

            

            