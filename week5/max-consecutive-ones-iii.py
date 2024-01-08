class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        prefix = left = right = max_ = 0
        while right < len(nums):
            prefix += nums[right]

            while prefix + k  < (right - left + 1):
                if nums[left] == 0:
                    left += 1
                else: 
                    prefix -= 1
                    left += 1
            max_ = max(max_, right - left + 1)
            right += 1
        return max_