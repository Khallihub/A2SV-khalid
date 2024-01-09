class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, curSum, = 0,0,0
        min_ = len(nums) + 1
        while right < len(nums):
            curSum += nums[right]
            while curSum >= target:
                min_ = min(min_, right-left+1)
                curSum -= nums[left]
                left += 1
            right += 1
        if min_ == len(nums)+1:
            return 0
        return min_