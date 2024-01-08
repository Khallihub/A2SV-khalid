class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1
        total = sum(nums[:k])
        res = float("-inf")
        while right < len(nums):
            res = max(res, total)
            total -= nums[left]
            left += 1
            right += 1
            if right < len(nums):
                total += nums[right]
        return res/k