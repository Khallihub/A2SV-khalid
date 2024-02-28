class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums.reverse()
        replacements = 0
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > last:
                ops = ceil(nums[i]/last)
                replacements += ops-1
                last = nums[i]//ops
            else: 
                last = nums[i]
        return replacements