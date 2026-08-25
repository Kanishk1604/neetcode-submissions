class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSub = nums[0]

        for num in nums:
            if total < 0:
                total = 0
                
            total += num
            maxSub = max(maxSub, total)

        return maxSub