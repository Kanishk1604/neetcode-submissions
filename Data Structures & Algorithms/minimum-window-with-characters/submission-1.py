class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #freqmapt
        #countS
        #iterate 
        if len(t) > len(s):
            return ""
        l = 0
        r = 0
        minwindow = float("inf")
        freqT = {}
        freqS = {}
        res = [-1, -1]
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)
        need = len(freqT)
        have = 0

        while r < len(s):
            c = s[r]
            freqS[c] = 1 + freqS.get(c, 0)

            if c in freqT and freqS[c] == freqT[c]:
                have += 1

            while have == need:
                if (r - l + 1 < minwindow):
                    minwindow = r - l + 1
                    res = [l,r]
                freqS[s[l]] -= 1
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        
        i, j = res 
        return "" if minwindow == float("inf") else s[i: j+1]