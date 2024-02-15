class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        maxSum = float("-inf")
        min_ = float("inf")
        for i in range(len(nums)):
            min_ = min(min_, runningSum)
            runningSum += nums[i]
            maxSum = max(maxSum, runningSum -( min_ if min_ < 0 else 0))
        return maxSum