class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxres = 0

        for num in numset:
            if (num - 1) not in numset:
                count = 1
                while num + count in numset:
                    count += 1
                maxres = max(maxres, count)

        return maxres