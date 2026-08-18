class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            rate = (l + r) // 2
            maxhrs = 0
            for p in piles:
                maxhrs += math.ceil(p / rate)
            
            if maxhrs <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return res


