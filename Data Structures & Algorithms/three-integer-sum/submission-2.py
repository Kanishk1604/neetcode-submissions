class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            if (nums[i] > 0):
                break
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = len(nums) - 1
            k = i + 1

            while k < j:
                sum = nums[i] + nums[k] + nums[j]

                if sum < 0:
                    k += 1
                elif sum > 0:
                    j -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k += 1
                    while(k < j and nums[k-1] == nums[k]):
                        k += 1
                    
            i += 1
        
        return res