class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map= {}

        for i in range(len(s)):
            freq_map[s[i]] = freq_map.get(s[i],0) + 1
        
        for i in range(len(t)):
            freq_map[t[i]] = freq_map.get(t[i],0) - 1
            if freq_map[t[i]] == 0:
                del freq_map[t[i]]
        
        return len(freq_map) == 0

        