class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= start:
                start = i
        
        return start == 0