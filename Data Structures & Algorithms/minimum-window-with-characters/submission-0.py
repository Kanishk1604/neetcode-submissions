class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = [-1, -1]
        reslen = float("infinity")

        countT = {}
        window = {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        have, need = 0, len(countT)

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
                p = s[l]
                window[p] -= 1
                if p in countT and window[p] < countT[p]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if reslen != float("infinity") else ""