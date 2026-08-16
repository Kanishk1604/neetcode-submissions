class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        leftMax, rightMax = height[left], height[right]
        amount = 0
        while left <= right:
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[left])
                amount += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                amount += rightMax - height[right]
                right -= 1

        return amount
