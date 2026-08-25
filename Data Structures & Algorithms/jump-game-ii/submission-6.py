class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            next_best = -1
            for i in range(l, r + 1):
                next_best = max(next_best, i + nums[i])
            
            l = r + 1
            r = next_best
            res += 1
        
        return res
        