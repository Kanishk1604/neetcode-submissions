class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seenSet = set()

        l, r = 0, 0 
        maxwindow = 0

        while r < len(s):
            c = s[r]
            
            while c in seenSet:
                seenSet.remove(s[l])
                l += 1
            
            maxwindow = max(maxwindow, r - l + 1)
            seenSet.add(c)
            r += 1
        
        return maxwindow

