class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}

        for c in s:
            freqS[c] = 1 + freqS.get(c, 0)
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)
        
        return True if freqS == freqT else False