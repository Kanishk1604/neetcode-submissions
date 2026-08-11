class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = float("infinity")

        while l <= r:
            mid = (l + r)//2
            #left side sorted
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])
                l = mid + 1
            else:   #right side sorted
                res = min(res, nums[mid])
                r = mid - 1
        
        return res