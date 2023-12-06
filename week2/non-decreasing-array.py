class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 0
        decreasing_count = 0
        increasing_count = 0
        max_ = nums[0]
        min_ = nums[-1]
        while i < len(nums):
            if nums[i] < max_:
                decreasing_count += 1
            if nums[len(nums)-i-1] > min_:
                increasing_count += 1
            max_ = max(max_, nums[i])
            min_ = min(min_, nums[len(nums)-i-1])
            if increasing_count >=2 and decreasing_count >= 2:
                return False
            i += 1
        return True