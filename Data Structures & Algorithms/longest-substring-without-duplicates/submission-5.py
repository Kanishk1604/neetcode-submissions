class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()

        l = 0
        r = 0
        maxwindow = 0

        while r < len(s):
            c = s[r]
            while c in seen:
                maxwindow = max(maxwindow, r - l)    
                seen.remove(s[l])
                l += 1
            seen.add(c)
            r += 1
        
        return max(maxwindow, r -l)