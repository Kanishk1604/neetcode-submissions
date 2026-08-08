class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [0] * len(nums)
        left_product[0] = nums[0]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i]

        right_product = [0] * len(nums)
        right_product[-1] = nums[-1]
        for i in range(len(nums)-2, 0, -1):
            right_product[i] = right_product[i+1] * nums[i]
        
        res = [0] * len(nums)
        res[0] = right_product[1]
        res[-1] = left_product[-2]

        for i in range(1, len(nums)-1):
            res[i] = left_product[i-1] * right_product[i+1]
        
        return res
