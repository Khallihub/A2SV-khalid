class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_ = 0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2] and nums[i]+nums[i+2]>nums[i+1] and nums[i+1]+nums[i+2]>nums[i]:
                max_ = max(max_, sum(nums[i:i+3]))
        return max_