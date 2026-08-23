class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        visit = set()
        l = 0
        r = 0
        window = 0
        while r < len(s):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            
            visit.add(s[r])
            window = max(window, r - l + 1)

            r += 1
        
        return window