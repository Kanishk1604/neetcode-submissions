class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for num in hashset:
            if (num-1) not in hashset:
                length = 0
                while num in hashset:
                    length += 1
                    num += 1
                longest = max(length, longest)
        
        return longest