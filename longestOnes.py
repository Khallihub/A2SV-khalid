class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for idx, val in enumerate(nums):
            k -= (1-val)
            if k < 0:
                k += (1-nums[left])
                left += 1
        return idx-left+1
