class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        left, right = 0,1
        unique = 0
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                nums[right] = "_"
                unique += 1
                right += 1
            left = right
            right += 1
        left,right = 0,0
        while right < len(nums):
            if type(nums[right]) == int:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return len(nums) - unique