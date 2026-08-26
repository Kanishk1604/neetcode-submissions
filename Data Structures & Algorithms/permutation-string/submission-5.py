class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqT = {}  #s1
        for c in s1:
            freqT[c] = 1 + freqT.get(c, 0)

        freqS = {}  #s2
        l, r = 0 ,0

        while r < len(s2):
            c = s2[r]
            freqS[c] = 1 + freqS.get(c, 0)
            
            if (r - l + 1) == len(s1):
                if freqS == freqT:
                    return True
                freqS[s2[l]] -= 1
                if freqS[s2[l]] == 0:
                    del freqS[s2[l]]
                l += 1
            r += 1
        
        return False
            

