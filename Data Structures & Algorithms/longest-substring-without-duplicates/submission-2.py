class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        i = 0
        j = 0
        seen = set()

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            seen.add(s[j])
            length = j - i + 1
            max_length = max(max_length, length)
            j += 1
        
        return max_length