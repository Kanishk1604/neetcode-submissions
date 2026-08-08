class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
    #[1,5,8,9,10,15,19] t = 24
    #   i            j

        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right +1]
    

        