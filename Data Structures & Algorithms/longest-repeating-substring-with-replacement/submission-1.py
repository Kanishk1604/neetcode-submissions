class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        maxwindow = 0
        maxf = 0
        l, r = 0, 0 

        while r < len(s):
            c = s[r]
            freqMap[c] = 1 + freqMap.get(c, 0)
            maxf = max(maxf, freqMap[c])

            while (r - l + 1) - maxf > k:
                freqMap[s[l]] -= 1
                l += 1
            
            maxwindow = max(maxwindow, r - l + 1)
            r += 1
        
        return maxwindow
        
