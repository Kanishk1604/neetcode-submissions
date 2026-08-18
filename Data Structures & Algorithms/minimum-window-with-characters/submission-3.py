class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = r = 0
        freqT = {}
        freqS = {}
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)
        have = 0
        seen = len(freqT)
        res = [-1, -1]
        minwindow = float("inf")
        while r < len(s):
            c = s[r]
            freqS[c] = 1 + freqS.get(c, 0)

            if c in freqT and freqS[c] == freqT[c]:
                have += 1
            
            while have == seen:
                ch = s[l]
                if r - l + 1 < minwindow:
                    minwindow = r - l + 1
                    res = [l, r]
                freqS[ch] -= 1
                if ch in freqT and freqS[ch] < freqT[ch]:
                    have -= 1
                l += 1
            r += 1
        left, right = res

        return "" if minwindow == float("inf") else s[left: right + 1]

