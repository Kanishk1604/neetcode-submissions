class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:   #left half sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:   #right halve sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

            