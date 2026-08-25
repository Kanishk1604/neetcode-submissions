class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqT = {}
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)
        
        freqS = {}
        seen = len(freqT)
        have = 0
        l, r = 0, 0
        minwindow = float("inf")
        res = [-1, -1]
        while r < len(s):
            c = s[r]
            freqS[c] = 1 + freqS.get(c, 0)

            if c in freqT and freqT[c] == freqS[c]:
                have += 1
            
            while have == seen:
                if (r - l + 1) < minwindow:
                    minwindow = r - l + 1
                    res = [l, r]
                k = s[l]
                freqS[k] -= 1
                if k in freqT and freqS[k] < freqT[k]:
                    have -= 1
                l += 1
            
            r += 1
        
        left, right = res
        
        return s[left:right + 1] if minwindow != float("inf") else ""
            