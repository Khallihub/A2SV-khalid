class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        good = len(nums)-1
        for i in range(1, len(nums)):
            if len(nums)-i-1 + nums[len(nums)-i-1] >= good:
                good = len(nums)-i-1
        if good == 0:
            return True
        return False