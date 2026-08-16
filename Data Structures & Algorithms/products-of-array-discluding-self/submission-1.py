class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left_product = [0] * n
        right_product = [0] * n

        left_product[0] = 1
        right_product[n - 1] = 1

        for i in range(1, n):
            left_product[i] = nums[i-1] * left_product[i-1]

        for i in range(n-2, -1, -1):
            right_product[i] = nums[i+1] * right_product[i+1]
        
        for i in range(n):
            res[i] = left_product[i] * right_product[i]

        return res
