class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0,0
        max_ = 0
        prefix = 0
        while right < len(nums):
            prefix += nums[right]
            while prefix < right - left:
                prefix -= nums[left]
                left += 1
            max_ = max(prefix, max_)
            right += 1
        if max_ == len(nums): return max_-1
        return  max_