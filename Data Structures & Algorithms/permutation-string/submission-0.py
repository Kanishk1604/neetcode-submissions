class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1count = {}
        s2count = {}

        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)

        if (s1count == s2count):
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            s2count[s2[right]] = 1 + s2count.get(s2[right], 0)
            s2count[s2[left]] -= 1

            if s2count[s2[left]] == 0:
                del s2count[s2[left]]
            
            left += 1

            if (s1count == s2count):
                return True
        
        return False