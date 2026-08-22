class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        
        l = 1
        r = max(piles) 
        

        while l <= r:
            mid = (l + r) // 2
            rate = 0
            for p in piles:
                rate += math.ceil(p / mid)

            if rate <= h:   
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

        