class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]

        left, right = 0, len(height)-1

        trapped = 0

        while left < right:
            min_ = min(leftMax, rightMax)
            if leftMax < rightMax:
                left += 1
                cur = min_ - height[left]  
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                cur = min_ - height[right]
                rightMax = max(rightMax, height[right])

            if cur > 0:
                trapped += cur
        
        return trapped
# 0 0 11 0 1
# 0 1 11 0 1
# 1 2 11 1 1
# 1 3 11 1 1
# 1 3 10 1 1
# 1 4 10 2 1
# 1 5 10 2 1
# 1 6 10 2 1
# 1 7 10 2 1
# 2 7 9 2 2
# 2 7 8 2 2