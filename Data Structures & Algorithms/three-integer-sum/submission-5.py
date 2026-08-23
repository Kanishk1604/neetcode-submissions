class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] > 0:
                break
            k = i + 1
            j = len(nums) - 1
            while k < j:
                sum = nums[i] + nums[k] + nums[j]

                if sum == 0:
                    res.append([nums[i], nums[k], nums[j]])
                    k += 1
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1
                elif sum < 0:
                    k += 1
                else:
                    j -= 1
            i += 1
        
        return res
