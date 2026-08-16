class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        freqs1 = {}
        freqs2 = {}

        for c in s1:
            freqs1[c] = 1 + freqs1.get(c, 0)
        
        l = 0
        r = 0
        count = 0
        while r < len(s2):
            c = s2[r]
            freqs2[c] = 1 + freqs2.get(c, 0)
            if c in freqs1:
                count += 1
            
            if (r - l + 1) == len(s1):
                if freqs1 == freqs2:
                    return True
                if s2[l] in freqs1:
                    count -= 1
                freqs2[s2[l]] -= 1
                if freqs2[s2[l]] == 0:
                    del freqs2[s2[l]]
                l += 1
            r +=1
        
        return False


