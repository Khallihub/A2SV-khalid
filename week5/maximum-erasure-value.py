class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right, score, cur = 0,0,0,0
        unique = set()
        while right < len(nums):
            while nums[right] in unique:
                unique.remove(nums[left])
                cur -= nums[left]
                left += 1
            unique.add(nums[right])
            cur += nums[right]
            score = max(score,cur)
            right += 1
        return score
