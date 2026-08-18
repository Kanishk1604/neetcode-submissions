class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hashSet = set(nums)
        maxres = 0

        for num in hashSet:
            if (num - 1) not in hashSet:
                length = 0
                while num in hashSet:
                    length += 1
                    num += 1
                maxres = max(maxres, length)
        
        return maxres
                
