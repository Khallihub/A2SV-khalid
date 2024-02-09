class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        middleIndex = -1
        for i in range(len(nums)):
            left += nums[i]
            right = total - left
            print(left, right)
            if left-nums[i] == right:
                return i
        return -1